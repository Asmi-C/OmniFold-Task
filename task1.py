#!/usr/bin/env python3
"""
inspect_omnifold_files.py

Utility script for Part 1 of the GSoC 2026 OmniFold evaluation task.

What it does:
- Opens the provided HDF5 files
- Prints HDF5 structure
- Loads the main pandas DataFrame from each file
- Lists columns, dtypes, shapes
- Classifies columns into observables, weights, and metadata/other
- Produces summary statistics
- Compares columns across files
- Writes a markdown report you can use as a draft for gap_analysis.md

Usage:
    python inspect_omnifold_files.py

Optional:
    python inspect_omnifold_files.py /path/to/multifold.h5 /path/to/multifold_sherpa.h5
"""

from __future__ import annotations

import os
import re
import sys
import math

import h5py
import numpy as np
import pandas as pd


# default file names to look for in the current directory
files=[
    "multifold.h5",
    "multifold_sherpa.h5",
    "multifold_nonDY.h5",
]

report="part1_file_inspection_report.md"


# ──────────────────────────────────────────────
# Small helper utilities
# ──────────────────────────────────────────────

def tofloat(x):
    """safely cast x to float, returning none on failure"""
    try:
        return float(x)
    except Exception:
        return None


def fmtnum(x, digits=6):
    """format a number for display, returns NA if x is none"""
    if x is None:
        return "NA"
    if isinstance(x, (int, np.integer)):
        return str(int(x))
    if isinstance(x, (float, np.floating)):
        return f"{x:.{digits}g}" if math.isfinite(x) else str(x)
    return str(x)


def tag(col):
    """
    classify a column name into one of four categories:
      weight     - any column that looks like an event weight
      observable - physics quantities like pt, eta, phi etc
      metadata   - bookkeeping columns like event id, run number etc
      other      - anything that does not match the above
    """
    c=col.lower()

    # weight columns usually contain the word weight or start with w
    if "weight" in c or c.startswith("w_") or c.startswith("weights_"):
        return "weight"

    # metadata columns relate to event or run bookkeeping, not physics
    metakeys=["event","run","dataset","sample","process","label","split",
              "seed","iteration","index","id","mcid","channel"]
    if any(k in c for k in metakeys):
        return "metadata"

    # physics observables follow standard hep naming patterns
    obspatterns=[r"^pt_",r"^eta_",r"^phi_",r"^y_",
                 r"^m_",r"^tau\d+_",r"^ntracks_"]
    if any(re.match(p, c) for p in obspatterns):
        return "observable"

    return "other"


# ──────────────────────────────────────────────
# File loading
# ──────────────────────────────────────────────

def gettree(path):
    """walk the hdf5 file and return a list of type:name strings"""
    out=[]
    with h5py.File(path, "r") as f:
        f.visititems(lambda name, obj: out.append(f"{type(obj).__name__}: {name}"))
    return out


def getkeys(path):
    """return all pandas hdfstore keys in the file"""
    with pd.HDFStore(path, mode="r") as store:
        return list(store.keys())


def loaddf(path):
    """
    load the main dataframe from the file.
    prefers the /df key if present, otherwise takes the first available key.
    returns (dataframe, key used).
    """
    keys=getkeys(path)
    if not keys:
        raise RuntimeError(f"no pandas keys found in {path}")
    key="/df" if "/df" in keys else keys[0]
    return pd.read_hdf(path, key=key), key


# ──────────────────────────────────────────────
# DataFrame summarization
# ──────────────────────────────────────────────

def summarize(df):
    """
    compute a summary dictionary for a dataframe.
    includes shape, column classification, missing value counts,
    numeric stats, and per-weight diagnostics.
    """
    info={}
    info["shape"]=df.shape
    info["columns"]=list(df.columns)

    # split columns into groups by category
    grp={"observable":[],"weight":[],"metadata":[],"other":[]}
    for col in df.columns:
        grp[tag(col)].append(col)
    info["groups"]=grp

    info["dtypes"]={col: str(dt) for col, dt in df.dtypes.items()}
    info["missing"]=df.isna().sum().to_dict()

    # numeric stats for every numeric column
    ns={}
    for col in df.select_dtypes(include=[np.number]).columns:
        s=df[col]
        ns[col]={
            "min": tofloat(s.min()),
            "max": tofloat(s.max()),
            "mean": tofloat(s.mean()),
            "std": tofloat(s.std()),
            "nunique": int(s.nunique(dropna=True)),
        }
    info["ns"]=ns

    # extra sanity checks for weight columns: sum, range, negative and zero counts
    wc={}
    for col in grp["weight"]:
        s=df[col]
        isnum=np.issubdtype(s.dtype, np.number)
        wc[col]={
            "sum": tofloat(s.sum()),
            "min": tofloat(s.min()),
            "max": tofloat(s.max()),
            "nneg": int((s<0).sum()) if isnum else None,
            "nzero": int((s==0).sum()) if isnum else None,
        }
    info["wc"]=wc

    return info


# ──────────────────────────────────────────────
# Cross-file column comparison
# ──────────────────────────────────────────────

def compare(res):
    """
    compare column sets across all successfully loaded files.
    returns:
      common - columns present in every file
      unique - columns not shared across all files, keyed by filename
    """
    cs={
        fn: set(d["summary"]["columns"])
        for fn, d in res.items()
        if "summary" in d
    }

    if not cs:
        return {"common":[],"unique":{}}

    common=set.intersection(*cs.values())

    # a column is unique to file x if it does not appear in every other file
    unique={fn: sorted(cols-common) for fn, cols in cs.items()}

    return {"common": sorted(common), "unique": unique}


# ──────────────────────────────────────────────
# Report generation
# ──────────────────────────────────────────────

def buildreport(res, comp):
    """render the inspection results as a markdown string"""
    out=[]
    out.append("# OmniFold File Inspection Report")
    out.append("")
    out.append("Generated automatically to support Part 1 (Exploration and Gap Analysis).")
    out.append("")

    for fn, d in res.items():
        out.append(f"## File: `{fn}`")
        out.append("")

        if "error" in d:
            out.append("**Status:** not processed")
            out.append(f"- Error: `{d['error']}`")
            out.append("")
            continue

        s=d["summary"]
        out.append(f"- Pandas key: `{d['key']}`")
        out.append(f"- Shape: **{s['shape'][0]} rows x {s['shape'][1]} columns**")
        out.append("")

        # raw hdf5 structure
        out.append("### HDF5 structure")
        out.append("")
        for line in d["tree"]:
            out.append(f"- {line}")
        out.append("")

        # column breakdown by category
        out.append("### Column classification")
        out.append("")
        for g in ["observable","weight","metadata","other"]:
            cols=s["groups"][g]
            out.append(f"- **{g}** ({len(cols)}): {', '.join(cols) if cols else 'None'}")
        out.append("")

        # flag any columns with missing values
        missing={k: v for k, v in s["missing"].items() if v>0}
        out.append("### Missing values")
        out.append("")
        if missing:
            for col, cnt in missing.items():
                out.append(f"- `{col}`: {cnt}")
        else:
            out.append("- No missing values detected.")
        out.append("")

        # weight diagnostics
        out.append("### Weight checks")
        out.append("")
        if s["wc"]:
            for col, st in s["wc"].items():
                out.append(
                    f"- `{col}`: "
                    f"sum={fmtnum(st['sum'])}, "
                    f"min={fmtnum(st['min'])}, "
                    f"max={fmtnum(st['max'])}, "
                    f"negative_count={st['nneg']}, "
                    f"zero_count={st['nzero']}"
                )
        else:
            out.append("- No weight columns identified.")
        out.append("")

        # observable ranges, first 12 only to keep report readable
        out.append("### Example observable ranges")
        out.append("")
        for col in s["groups"]["observable"][:12]:
            st=s["ns"][col]
            out.append(
                f"- `{col}`: "
                f"min={fmtnum(st['min'])}, "
                f"max={fmtnum(st['max'])}, "
                f"mean={fmtnum(st['mean'])}, "
                f"std={fmtnum(st['std'])}"
            )
        out.append("")

    # cross-file comparison section
    out.append("## Cross-file comparison")
    out.append("")
    out.append(f"- Common columns across all files ({len(comp['common'])}):")
    out.append("")
    for col in comp["common"]:
        out.append(f"  - `{col}`")
    out.append("")

    out.append("### File-specific columns")
    out.append("")
    for fn, cols in comp["unique"].items():
        out.append(f"- `{fn}` ({len(cols)} unique columns):")
        if cols:
            for col in cols:
                out.append(f"  - `{col}`")
        else:
            out.append("  - None")
    out.append("")

    return "\n".join(out)


def printsummary(res, comp):
    """print a full summary to the terminal including column names by category"""
    print("\n"+"="*80)
    print("CONSOLE SUMMARY")
    print("="*80)

    for fn, d in res.items():
        print(f"\nFILE: {fn}")
        if "error" in d:
            print(f"  ERROR: {d['error']}")
            continue

        sh=d["summary"]["shape"]
        print(f"  shape: {sh[0]} rows x {sh[1]} cols")

        # print each category with its count and the actual column names
        for g, cols in d["summary"]["groups"].items():
            print(f"\n  {g.upper()} ({len(cols)}):")
            if cols:
                for col in cols:
                    print(f"    - {col}")
            else:
                print("    (none)")

    print("\n"+"="*80)
    print("COMMON COLUMNS (present in all files):")
    print("="*80)
    for col in comp["common"]:
        print(f"  - {col}")

    print("\n"+"="*80)
    print("UNIQUE PER FILE (not shared across all files):")
    print("="*80)
    for fn, cols in comp["unique"].items():
        print(f"\n  {fn} ({len(cols)} unique):")
        if cols:
            for col in cols:
                print(f"    - {col}")
        else:
            print("    (none)")


# ──────────────────────────────────────────────
# Entry point
# ──────────────────────────────────────────────

def main():
    # accept file paths as command line arguments, fall back to defaults
    paths=sys.argv[1:] if len(sys.argv)>1 else files

    res={}

    for path in paths:
        fn=os.path.basename(path)
        d={}

        if not os.path.exists(path):
            d["error"]="file not found"
            res[fn]=d
            continue

        try:
            d["tree"]=gettree(path)
            df, key=loaddf(path)
            d["key"]=key
            d["summary"]=summarize(df)
        except Exception as e:
            d["error"]=str(e)

        res[fn]=d

    comp=compare(res)
    printsummary(res, comp)

    md=buildreport(res, comp)
    with open(report, "w", encoding="utf-8") as f:
        f.write(md)

    print(f"\nMarkdown report written to: {report}")


if __name__=="__main__":
    main()