# Day 2: Exploratory Data Analysis & Causal Balance Checks

## What I did
- Opened and executed `notebooks/01_eda.ipynb` on the Kevin Hillstrom Email Analytics dataset (64,000 customers).
- Analyzed the baseline conversion and visit rates across the three randomized treatment arms: `No E-Mail` (Control), `Mens E-Mail`, and `Womens E-Mail`.
- Calculated customer average spend across all three campaign arms.
- Generated bar charts comparing conversion rates and average customer revenue per segment.
- Computed Standardized Mean Differences (SMD) for all numerical and indicator pre-treatment covariates (`recency`, `history`, `mens`, `womens`, `newbie`).
- Created a Love plot to visualize covariate balance against the standard econometric threshold of $|SMD| < 0.10$.

## Key findings
- The control group (`No E-Mail`, 21,306 customers) had an organic conversion rate of 0.57% and an average spend of $0.653.
- The `Mens E-Mail` treatment arm (21,307 customers) achieved a 1.25% conversion rate (+0.68 percentage points uplift) and $1.423 average spend.
- The `Womens E-Mail` treatment arm (21,387 customers) achieved a 1.07% conversion rate (+0.50 percentage points uplift) and $1.077 average spend.
- Both email campaigns produced positive raw conversion lift over the control group.
- All pre-treatment covariates demonstrated $|SMD| < 0.015$ (for example, recency SMD was 0.0060 and past spend history SMD was 0.0071), confirming that treatment assignment was randomized cleanly without initial selection bias.

## Next steps
- Move to `notebooks/02_causal_graph.ipynb`.
- Formulate the Structural Causal Model (SCM) Directed Acyclic Graph (DAG).
- Evaluate propensity score overlap and test identification robustness using DoWhy falsification refuters.
