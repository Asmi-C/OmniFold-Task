# Part 1 – Exploration and Gap Analysis

## Overview

The provided files (`multifold.h5`,`multifold_sherpa.h5`, and `multifold_nonDY.h5`) contain event-level data representing the results of an OmniFold unfolding procedure applied to a Z+jets measurement.Each row corresponds to a single event and contains both physics observables and event weights used for reweighting.

Inspection of the files shows that they share a consistent set of physics observables but differ in the number and type of weight columns stored.

The structure of the files suggests that the nominal file contains the full uncertainty payload, while the other files represent systematic variations with reduced metadata.

---

# 1. Columns Present in the Files

### File sizes

| File | Rows | Columns |
|-----|------|------|
| `multifold.h5` | 418,014 | 200 |
| `multifold_sherpa.h5` | 326,430 | 51 |
| `multifold_nonDY.h5` | 433,397 | 26 |

Each row represents an event, while columns correspond to either observables or weights.

---

## Physics Observables

All three files share a consistent set of **24 physics observables** describing dilepton and jet kinematics.

Examples include:

### Lepton observables
- `pT_l1`, `pT_l2`
- `eta_l1`, `eta_l2`
- `phi_l1`, `phi_l2`

### Dilepton system
- `pT_ll`
- `y_ll`

### Track-jet observables
- `pT_trackj1`, `pT_trackj2`
- `phi_trackj1`, `phi_trackj2`
- `m_trackj1`, `m_trackj2`
- `tau1_trackj1`, `tau2_trackj1`, `tau3_trackj1`
- `tau1_trackj2`, `tau2_trackj2`, `tau3_trackj2`
- `Ntracks_trackj1`, `Ntracks_trackj2`

These observables correspond to the unfolded feature space used by OmniFold.

---

## Event Weights

Several types of weight columns are present.

### Core weights

These appear in all files:

- `weight_mc` — baseline Monte Carlo event weight  
- `weights_nominal` — nominal OmniFold reweighting factor  

These two weights are likely combined to obtain the final event weight.

---

### Bootstrap weights

Example:

```
weights_bootstrap_mc_0 ... weights_bootstrap_mc_24
weights_bootstrap_data_0 ... weights_bootstrap_data_24
```

These appear primarily in `multifold.h5` and represent **statistical resampling variations** used to estimate statistical uncertainties.

---

### Ensemble weights

Example:

```
weights_ensemble_0 ... weights_ensemble_99
```

These correspond to weights produced by multiple trained models in an ensemble and are likely used to estimate **machine-learning related uncertainties**.

---

### Systematic weights

Several columns correspond to detector or theory systematics, for example:

- `weights_muEffReco`
- `weights_muEffTrig`
- `weights_pileup`
- `weights_theoryPDF`
- `weights_theoryQCD`
- `weights_trackEffJet`

These encode variations used to propagate systematic uncertainties.

---

## Metadata

The files contain very little explicit metadata.

One column appearing only in the nominal file is:

```
target_dd
```

This likely corresponds to a training label used internally during the OmniFold procedure.

However, important contextual information such as event selection, normalization conventions, or object definitions is not encoded directly in the files.

---

# 2. Missing Information Needed for Reuse

Although the files contain all numerical inputs required to compute histograms, several pieces of information required for reliable reuse are missing.

### Observable definitions

The files list observable names but do not specify:

- units (GeV, radians, etc.)
- particle-level vs detector-level definitions
- jet reconstruction algorithms
- ordering conventions (e.g., leading vs subleading jet)

---

### Event selection

The files do not describe the fiducial selection applied to produce the dataset, such as:

- muon kinematic cuts
- jet requirements
- boosted regime definitions
- event cleaning or overlap removal

Without these definitions, reproducing the analysis phase space is difficult.

---

### Weight semantics

The files contain many weight columns but do not explicitly state:

- whether `weights_nominal` multiplies or replaces `weight_mc`
- which weight should be considered the central value
- how systematic weights should be interpreted (ratio vs replacement)
- whether negative weights are possible

---

### Normalization

The normalization convention is not specified. It is unclear whether:

- histograms should be normalized to cross section
- weights already include luminosity normalization
- the release is shape-only

---

### Provenance information

The files do not contain metadata describing:

- OmniFold training configuration
- number of unfolding iterations
- preprocessing steps
- software versions used for training

This information is useful for reproducibility and long-term preservation.

---

# 3. Challenges in Standardizing This Output

Standardizing OmniFold outputs across analyses and experiments introduces several challenges.

### Heterogeneous weight structures

The three files contain different numbers of weight columns:

| File | Weight Columns |
|-----|------|
| `multifold.h5` | ~175 |
| `multifold_sherpa.h5` | 27 |
| `multifold_nonDY.h5` | 2 |

This variation suggests that systematic and uncertainty information is encoded differently depending on the dataset.

---

### Naming conventions

Observable and weight names are analysis-specific. Without a standard naming schema, automated tools cannot reliably identify observables versus weight columns.

---

### Separation of core and auxiliary information

Some information is essential for reinterpretation (observables and nominal weights), while other information relates to uncertainty studies or training diagnostics. A standardized format must clearly separate these layers.

---

### Metadata placement

Currently, important information is spread across analysis papers, code repositories, and filenames rather than encoded directly in the data files. A standard publication format would require a structured metadata layer accompanying the event data.

---

# Summary

The files successfully provide the core numerical information needed for reinterpretation of the OmniFold result: event-level observables and weights. However, they lack several pieces of metadata required for robust reuse, including observable definitions, selection criteria, normalization conventions, and weight semantics.

A standardized publication framework should therefore include a machine-readable metadata file describing the dataset, observables, weight conventions, and systematic variations alongside the event-level data files.
