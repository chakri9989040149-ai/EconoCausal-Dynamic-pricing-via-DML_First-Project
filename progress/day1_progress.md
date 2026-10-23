# Day 1: Environment Setup and Project Initialization

## What I did
- Set up my local Python development environment for the EconoCausal project.
- Configured dependencies in `requirements.txt`, including core data science and causal inference packages (`pandas`, `numpy`, `scikit-learn`, `econml`, `dowhy`, `scipy`, `matplotlib`, `plotly`, and `jupyterlab`).
- Downloaded and verified the primary dataset for our study: the Kevin Hillstrom Email Analytics Challenge (`MineThatData`), placing it in `data/raw/hillstrom.csv`.
- Also placed smaller benchmark test fixtures in `data/fixtures/` (`hillstrom_fixture.csv` and `lalonde_fixture.csv`).
- Launched Jupyter Lab and verified that our Python environment and kernels were communicating properly.
- Created `src/utils.py` to hold clean, reusable data loading helper functions.

## Key findings
- The Hillstrom raw dataset loaded cleanly from disk, containing 64,000 customer records and 12 columns with customer purchase histories, visit flags, conversion flags, and randomized email segments.
- The Python virtual environment has all necessary C-extensions and numerical libraries installed (`econml`, `dowhy`, `scikit-learn`) ready for cross-fitting and refutations.

## Next steps
- Begin exploratory data analysis (EDA) in `notebooks/01_eda.ipynb`.
- Inspect conversion distributions across treatment segments and check covariate balance between treated and control groups using Standardized Mean Differences (SMD).
