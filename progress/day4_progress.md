# Day 4: Double Machine Learning & Estimator Benchmarking

## What I did
- Opened and executed `notebooks/03_estimators.ipynb`.
- Formulated the semi-synthetic customer pricing data generation process (2,500 records) with known ground-truth Individual Treatment Effects ($\tau^*$), introducing observational confounding into treatment assignment.
- Implemented `LinearDML` from EconML with 3-fold cross-fitting using `GradientBoostingRegressor` for outcome residualization and `LogisticRegression` for treatment propensity residualization.
- Fitted baseline meta-learners (S-Learner and T-Learner) using `GradientBoostingClassifier`.
- Calculated quantitative benchmark metrics for each model against the known ground-truth:
  - PEHE (Precision in Estimating Heterogeneous Effects)
  - ATE Error
  - CATE Pearson correlation coefficient ($r$)
- Generated a scatter plot of True ITE vs Estimated ITE with the reference diagonal line ($y = x$).
- Computed and plotted Cumulative Uplift curves (AUUC) comparing LinearDML against the S-Learner baseline and random selection.

## Key findings
- The true population Average Treatment Effect (ATE) was $\tau^* = 0.1036$.
- LinearDML estimated an ATE of $0.1182$ (an error of $0.0145$).
- In heterogeneous effect estimation, `LinearDML` outperformed all baselines:
  - **LinearDML:** PEHE = 0.0361, CATE correlation $r = 0.5489$.
  - **S-Learner:** PEHE = 0.0525, CATE correlation $r = 0.3180$.
  - **T-Learner:** PEHE = 0.0859, CATE correlation $r = 0.1970$.
- LinearDML achieved the lowest PEHE error and the highest correlation with individual treatment responses.
- The Cumulative Uplift curve demonstrated that targeting customers prioritized by LinearDML yields consistently higher cumulative conversions than the standard single-model baseline.

## Next steps
- Move to `notebooks/04_policy.ipynb`.
- Translate individual CATE estimates into actionable business policies using 4-quadrant uplift segmentation and solve the Multiple-Choice Knapsack problem for discount allocation under a campaign budget.
