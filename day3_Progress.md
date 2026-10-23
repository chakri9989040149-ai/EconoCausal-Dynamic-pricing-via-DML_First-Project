# Day 3: Structural Causal Model & Identification Refutations

## What I did
- Opened and executed `notebooks/02_causal_graph.ipynb`.
- Constructed and plotted a Directed Acyclic Graph (DAG) using NetworkX, identifying confounders (recency, past spend, loyalty, channel), treatment ($T$), and conversion outcome ($Y$), alongside latent unobserved confounders.
- Documented the three core causal identification axioms: Conditional Ignorability $(Y_0, Y_1) \perp T \mid X$, Common Support (Positivity), and SUTVA.
- Built a logistic regression propensity score model on 10,000 customer records to estimate $P(T=1 \mid X)$.
- Plotted the propensity score overlap between treated and control groups to verify common support.
- Computed the Kish Effective Sample Size (ESS) under Inverse Probability Weighting (IPW).
- Built a formal causal model in DoWhy, identified the backdoor estimand, calculated the baseline linear causal effect, and executed three falsification refutation tests: Random Common Cause, Placebo Treatment, and Data Subset (80% holdout).

## Key findings
- The propensity score overlap distribution confirmed strong common support, with both treated and control units distributed evenly across the range of scores.
- The Kish Effective Sample Size was calculated at 8,920 out of 10,000 customers (89.2% sample efficiency), indicating low variance inflation from extreme propensity weights.
- The baseline estimated causal effect was 0.0062 (~0.62 percentage points uplift).
- All three DoWhy refutation audits passed:
  - **Random Common Cause Refuter:** Original estimate 0.0062 $\rightarrow$ New estimate 0.0062 (PASS). Adding noise had no effect on the estimate.
  - **Placebo Treatment Refuter:** Original estimate 0.0062 $\rightarrow$ New estimate -0.0003 (PASS). Scrambling treatment caused the effect to drop to zero ($p > 0.05$).
  - **Data Subset Refuter (80% holdout):** Original estimate 0.0062 $\rightarrow$ New estimate 0.0062 (PASS). The estimate remained invariant across subsamples.

## Next steps
- Move to `notebooks/03_estimators.ipynb`.
- Implement Double Machine Learning (DML) using EconML's `LinearDML`.
- Benchmark against single-model (S-Learner) and two-model (T-Learner) baselines on semi-synthetic ground-truth data.
