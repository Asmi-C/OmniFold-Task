# Metadata Schema Design — Justification

## Overview

This document explains the design decisions behind `metadata.yaml`.

---

## Why I have used YAML here?

YAML was chosen because it is simultaneously machine-readable and
human-readable without requiring a special viewer. A physicist unfamiliar
with the analysis can open the file in any text editor and understand the
dataset before writing a single line of code. At the same time, downstream
tools can parse it with a single `yaml.safe_load()` call in Python. JSON
is also machine-readable, but it is less readable for humans and does
not support inline comments, which are important for documentation. A
domain-specific format (like ROOT TTrees with embedded headers) would
require special tooling and would not generalize across experiments.

---

## Structure and Rationale

The schema is organized into seven top-level sections. Each section
corresponds to a distinct information need.

### `dataset`

This section captures identity and provenance: the name, description,
experiment, DOI, and contact information. Without this block, a user who
downloads the files has no way to trace them back to a paper or responsible
person. The `analysis_label` field enables unambiguous referencing in
citations and downstream code.

### `generation`

This section records how the Monte Carlo simulation was produced: generator,
tune, parton shower, PDF set, and OmniFold configuration. This information
is essential for understanding the systematic uncertainty files, which
correspond to alternative generator choices. Fields like `n_ensemble_members`
and `n_bootstrap_replicas` are included because if it is not present then 
a user reading the file would have to count weight columns manually to 
understand the uncertainty structure.

### `event_selection`

The fiducial phase space definition is the most important missing piece in
the current files. Without knowing the lepton pT and eta cuts, the jet
algorithm and radius, and the mass window, a physicist cannot reproduce the
event selection, cannot check whether their own events fall inside the phase
space, and cannot interpret the unfolded result as a cross section
measurement. This section provides structured placeholders for all
standard selection criteria. For a real release, all null values would be
filled in.

### `observables`

Each observable is documented with a name (matching the HDF5 column name
exactly), a physics description, a unit, and the level (particle vs
detector). Units are deliberately required for every entry: GeV vs MeV
ambiguities have caused real problems in HEP data preservation. The
`level` field distinguishes particle-level (unfolded) quantities from
detector-level inputs, which is important because OmniFold produces
particle-level weights while the stored values may be particle-level Monte
Carlo quantities.

### `weights`

This is the most detailed section because weight semantics are the most
likely source of user confusion. Each weight entry specifies:

- a human-readable description,
- its `type` (core, statistical_uncertainty, ml_uncertainty, systematic, other),
- which files it appears in, and
- for the two core weights, an explicit `usage` instruction.

The explicit `usage` note for `weights_nominal` — stating that the final
weight is `weight_mc * weights_nominal` — directly addresses the gap
identified in Part 1. Without this, users would have to inspect the
OmniFold source code or contact the authors to know whether to multiply or
replace the MC weight.

Pattern entries (e.g., `weights_bootstrap_mc_{i}`) use an `index_range`
field to avoid listing 25 or 100 identical entries. A parsing tool can
expand these patterns programmatically.

### `systematic_files`

This section explicitly links the alternative HDF5 files to their physical
meaning. A user who downloads only `multifold.h5` would not know that
`multifold_sherpa.h5` exists or what it represents. By listing both files
here with descriptions and the `variation_type` field, the schema makes the
relationship between files explicit.

### `normalization` and `usage`

The `normalization` section records the luminosity and normalization
convention. The `usage` section provides step-by-step instructions for the
five main analysis workflows: nominal histogram, statistical uncertainty,
ML uncertainty, detector systematics, and generator/composition systematics.
These instructions are written in plain English so that a physicist who has
never used OmniFold can follow them without reading the original paper.

---

## What Was Left Out

Several pieces of information were deliberately excluded.

**Training configuration details** (learning rate, model architecture,
optimizer) were not included in the main schema because they belong to a
reproducibility layer rather than a reinterpretation layer. A user who wants
to reproduce the training should consult the code repository, not the
metadata file. Including them would add noise for the typical user.

**Per-column numeric statistics** (mean, standard deviation, min, max) were
not included because they are derivable from the data files and would bloat
the metadata. A separate companion script (such as `task1.py`) is the right
place for that information.

**Correlation structure of systematics** was not included because it is
analysis-specific and complex. A full covariance matrix would require a
different format (e.g., a separate JSON or NumPy file). The metadata schema
records what each systematic is. The correlation structure is left to the
analysis note.

---

## How a New User Would Interact With This File

A physicist receiving these files for the first time would follow this
workflow:

1. Open `metadata.yaml` to understand what the dataset is and where it came
   from (`dataset` section).
2. Read the `event_selection` section to determine whether their analysis
   phase space is compatible with the published result.
3. Consult the `observables` section to confirm units and definitions before
   plotting.
4. Read the `weights.usage` field for `weights_nominal` to learn how to
   apply the unfolded weights to produce a histogram.
5. Follow the `usage` section at the bottom to propagate uncertainties.

The schema is designed so that steps 1–5 can be completed without reading
any code or papers. This is the primary design goal: the metadata file
should be self-sufficient for a physicist performing reinterpretation.
