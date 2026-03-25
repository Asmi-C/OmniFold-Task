# Google Summer of Code 2026 Proposal
# Project: Omnifold-Publication of OmniFold Weights
## Standardizing the Publication, Preservation, and Reuse of ML-Based Unfolding Results

---

## Personal Information

| | |
|---|---|
| **Name** | Asmi Choudhary |
| **University** | IIT(Indian Institute of Technology), Kharagpur, India |
| **Degree** | B.Tech + M.Tech (Dual Degree), Computer Science and Engineering |
| **Year** | 3rd Year |
| **Year of Study** | 2023-2028 |
| **Email** | asmichoudhary03@gmail.com |
| **GitHub** | https://github.com/Asmi-C |
| **Linkedin** | https://www.linkedin.com/in/asmi-choudhary/ | 
|**Evaluation Task** | https://github.com/Asmi-C/OmniFold-Task |
| **Timezone** | IST (UTC +5:30) |

---

## Abstract

Modern unfolding methods like OmniFold ([arXiv:1911.09107](https://arxiv.org/abs/1911.09107)) represent a fundamental shift in how particle physics analyses are conducted—producing per-event weights and trained ML models instead of fixed binned histograms. While this offers extraordinary flexibility for reinterpretation, it simultaneously creates a critical gap: there is currently no standardized way to publish, preserve, or reuse these results.

This project will close that gap by building a complete publication ecosystem for OmniFold outputs. By the end of GSoC 2026, the deliverables will include: a formal YAML/JSON schema for OmniFold result metadata, a standardized HDF5 storage format for per-event weights, a Python package providing a user-facing API for loading and analyzing published results, a validation framework, reference end-to-end examples, and an integration layer with HEPData. Together, these components will enable the full pipeline:

> **Unfolding → Standardized Publication → HEPData Upload → Community Reinterpretation**

This project will establish a reusable standard for ML-based unfolding results, enabling long-term reproducibility and cross-experiment interoperability in high-energy physics.

---

## Motivation

### The Problem

OmniFold ([GitHub](https://github.com/hep-lbdl/OmniFold)) shifts the information content of an unfolded result from a fixed histogram to a set of per-event weights. This is powerful: a user can compute *any observable derived from available features* from the published weights without needing to rerun the experiment. However, in practice, these results cannot be reliably reused because:

1. **No metadata standard exists.** Observable names, units, phase-space cuts, and normalization conventions are not encoded in the output files themselves.
2. **Weight semantics are undocumented.** It is unclear to a new user whether nominal weights should multiply or replace Monte Carlo weights, how bootstrap replicas should be combined, or how systematic variations relate to the central value.
3. **File structures are heterogeneous.** Different OmniFold analyses encode weights using different naming patterns, index ranges, and groupings, making automated tooling impossible.
4. **HEPData integration is missing.** Existing HEPData infrastructure is designed for histograms. There is no pathway for publishing per-event weights in a way that is discoverable and usable by the community.

### Why This Matters Now

As OmniFold and related multidimensional unfolding methods become increasingly common in major LHC experiments, the absence of a publication standard risks creating a library of results that are individually correct but collectively unreusable. Establishing a standard now—while the community is still small and flexible—will have lasting impact on the reproducibility of ML-based physics analyses.

---

## Background Information

### What is Unfolding?

Particle physics detectors do not measure fundamental particle properties directly — they record detector-level signals that are smeared, distorted, and incomplete due to finite resolution, acceptance, and efficiency effects. *Unfolding* is the process of correcting for these detector effects to recover the underlying particle-level (truth-level) distributions, which can then be compared directly with theoretical predictions and with results from other experiments.

Traditional unfolding methods (e.g., iterative Bayesian unfolding, SVD) produce fixed binned histograms — a corrected distribution in a specific set of bins chosen at analysis time. This is robust and well-understood, but it limits the information available for reinterpretation: if a theorist wants to compare against a different binning, or compute a new observable, they cannot do so from the published histogram alone.

### What is OmniFold?

OmniFold ([arXiv:1911.09107](https://arxiv.org/abs/1911.09107), [GitHub](https://github.com/hep-lbdl/OmniFold)) is a machine-learning-based unfolding algorithm that overcomes this limitation. Instead of producing a binned histogram, OmniFold produces a **per-event weight** for every event in the Monte Carlo simulation. These weights reweight the simulation to match the data at the particle level.

The algorithm operates in two alternating steps:

- **Step 1:** Train a classifier to distinguish data from simulation at detector level; use the classifier output to reweight simulation events.
- **Step 2:** Train a classifier to distinguish reweighted from original simulation at particle level; use this to push the weights back to particle level.

These two steps alternate over several iterations until convergence. The final output is a set of weights — one per simulated event — that encode the unfolded result. Because the weights are defined on the full multidimensional space of particle-level observables, a user can compute *any observable derived from available features* after the fact, without needing to rerun the analysis.

OmniFold is available as a Python package ([PyPI](https://pypi.org/project/omnifold/)) and is increasingly being adopted by major LHC experiments for multidimensional unfolding measurements.

### What is HEPData?

[HEPData](https://www.hepdata.net/about) is the community repository for high-energy physics data. When a physics paper is published, the collaboration uploads their data tables, histograms, and supplementary materials to HEPData, making them citable, searchable, and reusable by the community. HEPData is the standard platform for data preservation and reinterpretation in HEP.

Currently, HEPData's infrastructure is designed around binned histograms and tables. There is no standard format or workflow for submitting OmniFold's per-event weights, which means that even when an OmniFold result is published, there is no established pathway to make it discoverable and usable through HEPData.

### The Gap This Project Fills

The OmniFold package handles *running* the algorithm — training the classifiers and computing the weights. What does not yet exist is the infrastructure for what comes after: how to store the weights in a standard format, how to document them so others can reuse them, how to validate that the weights are correct, and how to submit them to HEPData. This project builds that infrastructure end-to-end.

---

## Why This Project

My interest in this project is not incidental — it sits at the precise intersection of the two areas I have been building skills in throughout my undergraduate years: machine learning and rigorous scientific software engineering.

Through my coursework and independent projects, I have worked extensively with ML pipelines that produce probabilistic outputs — from Monte Carlo Dropout uncertainty quantification in image classification to ensemble-based uncertainty estimation in quantitative trading systems. What I kept encountering across these projects is the same problem OmniFold faces: ML models produce rich, high-dimensional outputs, but the infrastructure for sharing, validating, and reusing those outputs in a reproducible way almost never exists. You train a model, you get results, and then the results live in a private HDF5 file or a notebook that nobody else can use. Building the infrastructure to close that gap is exactly the kind of problem I find compelling.

High-energy physics is a domain where this problem is particularly consequential. The experiments at CERN — the scale of the data, the precision required, the years of effort that go into each measurement — mean that an unfolding result that cannot be reused is a genuine scientific loss. The OmniFold method is powerful precisely because it enables reinterpretation, but only if the publication infrastructure exists to support it. Contributing to that infrastructure, at this early stage when the community is still defining standards, is an opportunity to have a lasting impact that goes well beyond the GSoC period.

I am also drawn to the open-source, community-driven nature of the project. My IEEE Xplore publication on hybrid multi-objective optimization gave me early exposure to the process of formalizing and communicating technical results for a broader audience, and I want to continue working in that mode — building things that are designed from the start to be used, reviewed, and extended by others.

---

Before submitting this proposal, I completed the evaluation task assigned by the mentors. The repository is at: **https://github.com/Asmi-C/OmniFold-Task**

### What I did

**Part 1 — File Exploration and Gap Analysis (`gap_analysis.md`, `task1.py`)**

I performed a systematic inspection of the three provided HDF5 files (`multifold.h5`, `multifold_sherpa.h5`, `multifold_nonDY.h5`), which together represent a Z+jets OmniFold unfolding result. Key findings:

- All three files share 24 physics observables (lepton kinematics, dilepton system, track-jet substructure), but the weight structures differ dramatically: `multifold.h5` has ~175 weight columns while `multifold_nonDY.h5` has only 2.
- The files contain nominal OmniFold weights (`weights_nominal`), bootstrap replicas (`weights_bootstrap_mc_{i}`, `weights_bootstrap_data_{i}`), ensemble weights (`weights_ensemble_{i}`), and named systematics (`weights_muEffReco`, `weights_theoryPDF`, etc.), but nowhere specify how these weights interact or how they should be combined.
- Critical metadata is absent: observable units, fiducial selection cuts, normalization conventions, and OmniFold training configuration are all missing from the files themselves.

The full gap analysis is documented in [`gap_analysis.md`](https://github.com/Asmi-C/OmniFold-Task/blob/main/gap_analysis.md), and a programmatic inspection script is in [`task1.py`](https://github.com/Asmi-C/OmniFold-Task/blob/main/task1.py).

**Part 2 — Metadata Schema Design (`metadata.yaml`, `schema_design.md`)**

Based on the gap analysis, I designed a seven-section YAML metadata schema:

- `dataset` — identity and provenance (name, DOI, experiment, contact)
- `generation` — Monte Carlo and OmniFold configuration (generator, tune, PDF set, n_iterations, n_ensemble_members, n_bootstrap_replicas)
- `event_selection` — fiducial phase space definition (lepton cuts, jet algorithm and radius, mass window)
- `observables` — per-column documentation with name, description, unit, and particle/detector level
- `weights` — explicit semantics for every weight type, including a `usage` field explaining how `weight_mc` and `weights_nominal` combine to give the final event weight
- `systematic_files` — explicit links between alternative HDF5 files and their physical meaning
- `normalization` and `usage` — step-by-step instructions for five analysis workflows

The schema design rationale is documented in [`schema_design.md`](https://github.com/Asmi-C/OmniFold-Task/blob/main/schema_design.md).

**Part 3 — Weighted Histogram Implementation (`weighted_histogram.py`)**

I implemented a `compute_weighted_histogram` function that takes events, an observable name, binning, and a weight column specification, and correctly applies the combined weight (`weight_mc × weights_nominal`). The function includes basic validation (normalization check, negative weight warning).

### Key Insights That Shaped This Proposal

The evaluation task gave me concrete experience with exactly the problems this project must solve. The most important insight: *the gap is not in the numerical data but in the surrounding context*. The files contain everything needed to compute histograms, but a physicist receiving them for the first time cannot reliably reproduce a result without significant reverse engineering. This proposal directly addresses that gap through a metadata-first design philosophy.

### Head Start from the Evaluation Task

Several components of this project are not starting from scratch, because the evaluation task was explicitly designed to mirror the project's core deliverables:

| Evaluation Task Deliverable | Corresponding Project Task | Status |
|---|---|---|
| `metadata.yaml` — seven-section YAML schema | Task 1: Data & Metadata Specification | **Largely complete.** Needs JSON Schema formalization and validation tooling. |
| `schema_design.md` — full design rationale | Task 1: Data & Metadata Specification | **Complete.** Will be incorporated into project documentation. |
| `gap_analysis.md` — systematic file inspection and gap identification | Task 2: Per-Event Weight Storage (weight structure analysis) | **Complete** as analysis. HDF5 group hierarchy and conversion utility still to build. |
| `weighted_histogram.py` — `compute_weighted_histogram` function | Task 5: Analysis & Reinterpretation API | **Prototype complete.** Full API (uncertainty propagation, plotting, HEPData loading) still to build. |

This means the project is de-risked from the start: the metadata schema has already been validated against real OmniFold output files, the weight semantics have been worked out from first principles, and the core compute function is already tested. GSoC time can be spent on the harder engineering problems — the standardized storage format, the full Python package, the validation framework, and the reference examples — rather than on exploratory design work that is already done.

---

## Plan of Action

**This proposal prioritizes Tasks 1–6 and Task 8 as core deliverables within the 175-hour timeline. Task 7 (HEPData integration) is treated as a stretch goal to be completed if time permits.**

The full pipeline this project implements end-to-end:

```
OmniFold Weights → Standard Format → Metadata Schema → Python API → Validation → HEPData → Community Users
```

Each component is independently useful, ensuring value even without stretch goals.

### Task 1 — Data and Metadata Specification

**Goal:** Define a machine-readable schema that captures everything a physicist needs to reuse an OmniFold result without reading the original paper.

Building directly on `metadata.yaml` from my evaluation task, I will formalize the schema with:

- **JSON Schema validation** (`schema.json`) with required vs optional fields and type checking
- **Seven structured sections** as designed in the evaluation task, with field-level documentation
- **Pattern-based weight entries** using `index_range` to compactly describe bootstrap/ensemble groups without listing hundreds of identical entries
- **Cross-file linking** in the `systematic_files` section to make relationships between HDF5 files explicit

Example of the weight semantics section (extending my existing design):

```yaml
weights:
  - name: weights_nominal
    description: OmniFold reweighting factor from the final unfolding iteration
    type: core
    usage: "Final event weight = weight_mc * weights_nominal"
  - name: weights_bootstrap_mc_{i}
    description: Bootstrap replica weights for statistical uncertainty estimation
    type: statistical_uncertainty
    index_range: [0, 24]
    usage: "Compute histogram for each i; RMS across replicas gives statistical uncertainty"
  - name: weights_ensemble_{i}
    description: Weights from individual ensemble members
    type: ml_uncertainty
    index_range: [0, 99]
    usage: "RMS across ensemble members gives ML-related uncertainty"
```

**Deliverables:** `schema.yaml`, `schema.json` (JSON Schema), validation utilities (`validate_schema.py`), schema documentation.

---

### Task 2 — Per-Event Weight Storage Format

**Goal:** Define a standard HDF5 container structure that is unambiguous, scalable, and compatible with both Python and C++ HEP tools.

The key design challenge is that the three files from the evaluation task already use HDF5 but with flat, analysis-specific column naming. The standard format will impose explicit group hierarchy:

```
result.h5
├── events/
│   ├── pT_l1         (float32, shape: [N])
│   ├── eta_l1        (float32, shape: [N])
│   └── ...           (all 24+ observables)
├── weights/
│   ├── nominal       (float64, shape: [N])
│   ├── mc_weight     (float64, shape: [N])
│   ├── bootstrap/
│   │   ├── mc        (float64, shape: [N, n_replicas])
│   │   └── data      (float64, shape: [N, n_replicas])
│   ├── ensemble      (float64, shape: [N, n_members])
│   └── systematics/
│       ├── muEffReco (float64, shape: [N])
│       ├── theoryPDF (float64, shape: [N])
│       └── ...
└── metadata          (JSON string in HDF5 attribute, linking to schema)
```

Key design decisions:
- Bootstrap and ensemble weights stored as 2D arrays `[N, n_replicas]` rather than separate named columns — this is both more efficient and makes the structure self-describing
- Metadata embedded as a JSON attribute so the file is self-contained
- Explicit separation of `events/` (observables) from `weights/` (reweighting) to avoid naming collisions

**Deliverables:** Format specification document, `convert_to_standard.py` (conversion utility for existing files), format validation tests.

---

### Task 3 — Model and Training Details

**Goal:** Define what training metadata should be stored alongside the weights to enable reproducibility.

I will define two publication tiers:

- **Minimal (required):** Number of iterations, ensemble size, bootstrap size, input feature list, preprocessing method (standardization parameters), OmniFold version
- **Full (optional):** Model architecture definition (JSON or ONNX), training hyperparameters, optimizer state, per-iteration convergence diagnostics

The distinction matters because most users want to *reinterpret* results, not *retrain* the model. The minimal tier provides everything needed for reinterpretation. The full tier enables independent validation and retraining.

**Deliverables:** Training metadata specification, `save_model_metadata.py` utility, documentation of required vs optional fields.

---

### Task 4 — Observable Definitions

**Goal:** Provide a Python interface for defining physics observables with units, cuts, and binning, ensuring that published observables are fully reproducible.

```python
from omnifold_pub import Observable

obs = Observable(
    name="pT_ll",
    description="Transverse momentum of the dilepton system",
    unit="GeV",
    level="particle",
    column="pT_ll",
    bins=np.linspace(0, 600, 31),
    cuts=["abs(eta_l1) < 2.5", "abs(eta_l2) < 2.5", "pT_l1 > 27", "pT_l2 > 25"],
)
```

Observable definitions will be serializable to/from YAML so they can be stored alongside the data and shared in analysis notes. I will provide reference implementations for all 24 observables present in the evaluation task dataset.

**Deliverables:** `Observable` class, YAML serialization, reference observable library, Jupyter notebook demonstrating observable computation.

---

### Task 5 — Analysis and Reinterpretation API

**Goal:** A user-facing Python package (`omnifold_pub`) that lets physicists load published results, apply weights, compute observables, and propagate uncertainties — without needing to understand the internal weight structure.

Core API design:

```python
from omnifold_pub import load_result, compute_observable, plot_result

# Load a published result (locally or from HEPData)
result = load_result("path/to/result.h5", metadata="path/to/metadata.yaml")

# Compute a histogram with full uncertainty breakdown
hist = compute_observable(
    result,
    observable=obs,
    uncertainty=["statistical", "ml", "systematics"],
)

# Publication-quality plot
plot_result(hist, label="OmniFold result", save="pT_ll.pdf")
```

The `compute_observable` function will correctly handle:
- Nominal histogram: `weight_mc × weights_nominal`
- Statistical uncertainty: RMS over bootstrap replicas
- ML uncertainty: RMS over ensemble members
- Systematic uncertainty: envelope or explicit per-source variations
- Combined uncertainty: quadrature sum with configurable correlation assumptions

The API will also include a `load_from_hepdata(inspire_id, table_name)` function as the primary entry point for community users.

**Deliverables:** `omnifold_pub` Python package (installable via pip), API documentation, uncertainty propagation tutorial notebook.

---

### Task 6 — Validation Framework

**Goal:** Standardized validation procedures that can be run on any OmniFold result to check correctness before publication.

Validation checks:

| Check | Description | Pass/Fail Criterion |
|---|---|---|
| Closure test | Re-weight MC to MC; result should reproduce input distribution | e.g., KS test or χ² test depending on observable |
| Normalization | Total weight should be consistent with expected normalization (cross-section × luminosity, if available); if not available, fall back to shape-only check — verify weights sum to a stable value across iterations and that no single event dominates | < 1% deviation (absolute), or stable to < 1% across iterations (shape-only) |
| Iteration stability | Weights should converge across iterations | RMS change < configurable threshold |
| Bootstrap coverage | Bootstrap uncertainty should match Poisson expectation on toy datasets | Within 10% |
| Negative weight fraction | Flag datasets with high negative weight fraction | Warning above configurable threshold (default 5%) |
| Schema compliance | Metadata file passes JSON Schema validation | Hard pass/fail |

**Deliverables:** `validate_result.py` CLI tool, `ValidationReport` class with structured output, CI-friendly exit codes, example validation notebook.

---

### Task 7 — HEPData Integration (Stretch Goal)

**Goal:** A submission pathway that maps OmniFold outputs to HEPData records, enabling discovery through the standard HEP data portal.

The HEPData format ([hepdata.net](https://www.hepdata.net/about)) expects YAML submission files with structured tables. For OmniFold, the mapping is non-trivial because HEPData is designed for histograms. The integration layer will:

- Generate HEPData-compatible YAML submission files from OmniFold metadata
- Represent the per-event weight file as a linked resource (large file attachment)
- Provide submission templates and a step-by-step submission guide
- Include validation steps to check HEPData compatibility before submission

**Deliverables (if time allows):** `generate_hepdata_submission.py`, submission template YAML, integration guide, example submission for the evaluation task dataset.

---

### Task 8 — End-to-End Reference Examples

**Goal:** Complete, runnable examples that demonstrate the full pipeline from OmniFold output to published result to community reinterpretation.

Three reference notebooks using the public evaluation task dataset:

1. **Publisher notebook:** "How to publish your OmniFold result"
   - Convert existing HDF5 files to standard format
   - Write metadata YAML
   - Run validation checks
   - (Optionally) prepare HEPData submission

2. **Consumer notebook:** "How to use a published OmniFold result"
   - Load result from standard format
   - Reproduce published observables
   - Compute a new observable not in the original publication
   - Propagate statistical and systematic uncertainties

3. **Comparison notebook:** "Comparing OmniFold results across generators"
   - Load nominal, Sherpa, and non-DY files
   - Produce comparison plots with proper uncertainty treatment

**Deliverables:** Three Jupyter notebooks, `README.md` with quickstart instructions, companion dataset (converted from evaluation task files).

---

## Technical Implementation Plan

### Package Architecture

```
omnifold_pub/
├── __init__.py
├── schema/
│   ├── schema.yaml          # Human-readable specification
│   ├── schema.json          # JSON Schema for validation
│   └── validate.py          # Schema validation utilities
├── io/
│   ├── reader.py            # Load standard HDF5 format
│   ├── writer.py            # Write standard HDF5 format
│   └── convert.py           # Convert existing files to standard format
├── observable.py            # Observable class and reference library
├── analysis.py              # compute_observable, uncertainty propagation
├── plot.py                  # Publication-quality plotting
├── validation/
│   ├── closure.py
│   ├── normalization.py
│   └── report.py
└── hepdata/                 # (Stretch) HEPData integration
    ├── submission.py
    └── templates/
```

### Tech Stack

- **Python 3.10+**, NumPy, h5py, pandas, PyYAML, jsonschema
- **Matplotlib / mplhep** for publication-quality HEP-style plots
- **pytest** for unit and integration tests
- **Jupyter** for reference notebooks
- **GitHub Actions** for CI (tests + validation on example dataset)

---

## Timeline

### Community Bonding Period

- Deep dive into the OmniFold codebase and the public Z+jets example
- Study existing HEPData submission format in detail
- Discuss schema design decisions with mentors; finalize required vs optional fields
- Set up CI infrastructure and package skeleton

### Week 1–2 — Schema and Storage Format

- Finalize and document the YAML/JSON schema (Task 1)
- Implement JSON Schema validation and write tests
- Design and document the HDF5 group hierarchy (Task 2)
- Implement `convert_to_standard.py` and test against the three evaluation task files

### Week 3–4 — Observable Interface and Model Metadata

- Implement the `Observable` class with YAML serialization (Task 4)
- Write reference observable definitions for all 24 observables in the evaluation dataset
- Define and document the model metadata specification (Task 3)
- Write unit tests for all above

**Milestone (end of Week 4):** Schema validated, standard HDF5 files produced from evaluation task dataset, all 24 observables defined.

### Week 5–7 — Analysis API

- Implement `load_result`, `compute_observable` with full uncertainty propagation (Task 5)
- Implement `plot_result` with mplhep styling
- Implement `load_from_hepdata` stub (returns informative error until HEPData integration is complete)
- Write comprehensive tests; compare output against manual numpy calculations to verify correctness

**Midterm Evaluation:** Milestone submission — working API that can load evaluation task files, compute all 24 observables with statistical and systematic uncertainties, and produce publication-quality plots.

### Week 8–9 — Validation Framework

*(College semester begins mid-July; available evenings IST)*

- Implement all six validation checks (Task 6)
- Implement `ValidationReport` class and CLI tool
- Test closure check on evaluation task dataset (MC-to-MC reweighting)
- Test normalization check with known cross section

**Milestone (end of Week 9):** `validate_result.py` runs on evaluation task dataset and produces structured report.

### Week 10–11 — Reference Examples and HEPData (Stretch)

*(College semester ongoing; available evenings IST)*

- Write all three reference Jupyter notebooks (Task 8)
- If time allows: implement HEPData submission generator (Task 7)
- User testing: have the notebooks reviewed by a physicist unfamiliar with the code
- Fix any usability issues identified

### Week 12 — Polish, Documentation, Packaging

- Finalize API documentation (docstrings + Sphinx)
- Write `README.md` with installation and quickstart
- Package for PyPI (`setup.py` / `pyproject.toml`)
- Final review with mentors
- Submit final work product

---

## Expected Deliverables Summary

By the end of GSoC 2026:

| Deliverable | Status |
|---|---|
| Formal YAML/JSON schema for OmniFold results | Core |
| JSON Schema validation utilities | Core |
| Standardized HDF5 storage format specification | Core |
| File conversion utility (`convert_to_standard.py`) | Core |
| `Observable` class with reference library | Core |
| Model/training metadata specification | Core |
| `omnifold_pub` Python package (pip-installable) | Core |
| Weighted histogram + uncertainty propagation API | Core |
| Publication-quality plotting utilities | Core |
| Validation framework (`validate_result.py`) | Core |
| Three end-to-end reference Jupyter notebooks | Core |
| HEPData submission generator | Stretch |
| HEPData integration guide | Stretch |

---

## Risks and Mitigation

| Risk | Mitigation |
|---|---|
| **Large dataset handling** — OmniFold files can contain hundreds of weight columns across hundreds of thousands of events | Optimized HDF5 structure with chunking and compression; 2D array storage for bootstrap/ensemble weights avoids column explosion |
| **Ambiguity in weight semantics** — different analyses may combine weights differently | Resolve through early mentor discussions in community bonding; encode decisions explicitly in schema; validation framework catches incorrect combinations |
| **HEPData integration complexity** — HEPData infrastructure is designed for histograms, not per-event weights | Treated as stretch goal from the start; core deliverables are fully independent of HEPData |
| **Time constraints during semester** — college semester begins mid-July | All six core tasks (1–6) are front-loaded in Weeks 1–9, completing before or at the midterm; Weeks 10–12 cover reference examples and polish which are more flexible |
| **Schema design disagreements with mentors** | Schema designed iteratively during community bonding before coding begins; evaluation task schema provides a concrete starting point for discussion rather than a blank slate |

---

## Communication Plan

- **Weekly written updates** to mentors via email or GitHub, summarising progress, blockers, and next steps
- **GitHub Issues** used for all task tracking — one issue per deliverable, with linked PRs for review
- **Design discussions** held before each major component begins (schema, storage format, API design) to ensure alignment before implementation
- **Mentor office hours** attended regularly; questions batched and prepared in advance to make sessions efficient
- I am comfortable with async communication and will respond promptly across IST and US time zones

---

## About Me

I am a 2nd-year B.Tech + M.Tech (Dual Degree) student in Computer Science and Engineering at IIT Kharagpur. My primary research interests are scientific software engineering, machine learning, and data-driven workflows.

**Technical skills:**

- **Languages:** Python, C++, C, SQL
- **ML/DL:** Scikit-Learn, PyTorch; CNN, LSTM, ANN, Random Forest, XGBoost, Bayesian Optimization, Monte Carlo Dropout
- **Scientific computing:** NumPy, Pandas, Matplotlib, h5py; experienced with HDF5 and Parquet at scale
- **Software engineering:** Git, Linux, CI/CD, pytest, PyPI packaging, Sphinx documentation
- **Certifications:** Machine Learning Specialization (Stanford University), Graph Theory (UC San Diego)

**Most relevant projects:**

- **CNN with Uncertainty Quantification** *(Mentor: Prof. Amit Ghosh)* — Built a CNN with Monte Carlo Dropout for probabilistic uncertainty estimation, achieving 92% validation accuracy under noisy conditions. This experience with ensemble-style uncertainty quantification maps directly onto OmniFold's bootstrap and ensemble uncertainty framework.

- **RL-Based Quantitative Trading System** *(Mentor: Dr. A. Chavan)* — Designed an RL pipeline integrating LSTM forecasting, Bayesian optimization, and weighted statistical validation over a 2-year multi-asset backtest (Sharpe 1.22, 30.3% cumulative return). Directly relevant to this project's weighted analysis and uncertainty propagation components.

- **Estate Predict: ML Data Pipeline** — Engineered an end-to-end ML pipeline (Python, Scikit-Learn, Pandas, NumPy, Django) with automated ETL. Directly relevant to the HDF5 I/O, format conversion, and schema validation components of this project.

- **IEEE Xplore Publication (2022), Crest Gold Award — British Science Association UK** — *Intelligent Hybrid Multi-Objective Optimization Model*, hybrid ANN-TOPSIS framework, 3.5× RAE gain. [[Link]](https://bit.ly/4bZ8frT)

**Why I am the right person for this project:**

I completed the evaluation task before writing this proposal, and that work directly shapes every design decision here. My gap analysis identified the specific missing information in real OmniFold output files. My metadata schema addresses those gaps with explicit justification for every field — and it is already functional, having been designed against actual data rather than hypothetical requirements. Experience with Monte Carlo Dropout uncertainty quantification, end-to-end data pipelines, and weighted statistical analysis means the hardest parts of this project — uncertainty propagation, HDF5 format design, and validation — are all within my demonstrated competence.

I am applying only to this project within GSoC 2026.

---

## Post-GSoC Plans

I intend to continue contributing to the OmniFold ecosystem after GSoC ends. Specific plans:

- Maintain the `omnifold_pub` package and respond to community bug reports
- Work with the OmniFold maintainers to integrate the standard format directly into the main OmniFold codebase, so that standardized publication is the default output rather than an add-on
- Extend the framework to support other ML-based unfolding methods (e.g., MultiFold variants, flow-based unfolding) as they emerge
- Present the project at a relevant workshop (e.g., CHEP, ACAT) if the opportunity arises

---

## Availability

I am available full-time during the GSoC period (June–October). My college semester begins in mid-July; from that point I will be available in the evenings IST after classes, and I am fully committed to ensuring the project is completed with all expected results within the timeline. I am flexible with meeting times and comfortable with asynchronous communication across time zones. I will proactively keep mentors informed of any schedule changes.

---

## References

- OmniFold paper: [arXiv:1911.09107](https://arxiv.org/abs/1911.09107)
- OmniFold GitHub: [hep-lbdl/OmniFold](https://github.com/hep-lbdl/OmniFold)
- OmniFold PyPI: [omnifold](https://pypi.org/project/omnifold/)
- HEPData: [hepdata.net](https://www.hepdata.net/about)
- Evaluation task repository: [Asmi-C/OmniFold-Task](https://github.com/Asmi-C/OmniFold-Task)
