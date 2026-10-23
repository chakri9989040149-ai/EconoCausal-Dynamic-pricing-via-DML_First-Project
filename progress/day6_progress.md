# Day 6: Counterfactual What-If Simulator & Uncertainty Bounds

## What I did
- Opened and executed `notebooks/05_whatif_simulation.ipynb`.
- Implemented a counterfactual customer simulation function that predicts individualized uplift across discrete discount tiers ($0, $10, $20) as a function of customer loyalty, recency, historical spend, and browsing channel.
- Computed asymptotic 95% confidence intervals (CI) for treatment effect predictions:
  $$\hat{\tau} \pm 1.96 \cdot \text{SE}$$
- Simulated and compared two representative customer personas:
  - **VIP Shopper:** High loyalty (0.85), frequent/recent visits (recency 2.0 months), web channel.
  - **At-Risk Shopper:** Low loyalty (0.25), dormant (recency 14.0 months), offline channel.
- Plotted comparative bar charts of predicted conversion uplift with 95% confidence intervals.
- Performed a continuous sensitivity sweep across customer loyalty (0.05 to 0.95) for both $10 and $20 discount tiers and plotted the continuous uplift response curves against the zero-uplift boundary.

## Key findings
- For the VIP customer profile:
  - $10 coupon predicted uplift: **13.2%** [95% CI: 10.8% to 15.6%].
  - $20 coupon predicted uplift: **19.8%** [95% CI: 16.7% to 22.9%].
  - The confidence intervals are strictly positive and bounded away from zero, indicating high confidence in strong promotional responsiveness.
- For the At-Risk customer profile:
  - $10 coupon predicted uplift: **4.0%** [95% CI: 1.6% to 6.4%].
  - Lower baseline and smaller marginal uplift do not justify higher coupon tier costs ($20), as incremental margin fails to offset discount depth.
- The continuous loyalty sensitivity plot showed that uplift scales monotonically with customer loyalty, confirming that discounts are most effective when paired with engaged customers rather than as blunt instruments for dormant users.

## Next steps
- Complete `progress/day7_progress.md` with final synthesis, overall methodology review, and project summary.
