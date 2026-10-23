# Day 5: Policy Optimization & Knapsack Budget Allocation

## What I did
- Opened and executed `notebooks/04_policy.ipynb`.
- Categorized 2,000 customers into the 4-quadrant uplift segmentation framework: Persuadables, Sure Things, Lost Causes, and Sleeping Dogs based on baseline conversion probability ($Y_0$) and predicted treatment effect ($\hat{\tau}$).
- Set up the Multiple-Choice Knapsack Problem (MCKP) mathematical optimization model to allocate discrete coupon tiers ($0, $10, $20) to maximize net incremental gross profit:
  $$\pi_{i,k} = \hat{\tau}_{i,k} \times \text{Margin} - \text{Cost}_k$$
- Implemented an allocator subject to a budget constraint and negative uplift suppression.
- Solved the allocation for a $5,000 campaign budget assuming an $80 gross margin per converted purchase.
- Conducted a budget sensitivity analysis by sweeping budget levels from $1,000 to $20,000 and plotting expected incremental profit against budget size.
- Generated a customer-level allocation sample table displaying assigned discount tiers.

## Key findings
- Customer segmentation distribution on the 2,000 customer cohort:
  - **Persuadables:** 975 customers (48.8% share, mean baseline $Y_0 = 13.7\%$, mean uplift $\hat{\tau} = +8.03\%$). Recommended for primary promotion.
  - **Sure Things:** 529 customers (26.5% share, mean baseline $Y_0 = 30.8\%$, mean uplift $\hat{\tau} = +5.78\%$). Recommended to withhold discounts because they buy organically.
  - **Lost Causes:** 380 customers (19.0% share, mean baseline $Y_0 = 14.1\%$, mean uplift $\hat{\tau} = +1.99\%$). Recommended to withhold discounts due to low responsiveness.
  - **Sleeping Dogs:** 116 customers (5.8% share, negative uplift). Strictly suppressed from outreach.
- Under a $5,000 campaign budget, the optimizer allocated $1,050.00 across 105 customers with the highest marginal return, generating an expected incremental profit of $149.04 above coupon costs.
- The budget sensitivity curve revealed a diminishing marginal return pattern: profits rise sharply initially as high-uplift Persuadables are funded, reaching an inflection point around $7,500 where remaining unallocated customers yield sub-marginal returns.

## Next steps
- Move to `notebooks/05_whatif_simulation.ipynb`.
- Build counterfactual simulations for specific customer profiles, assess 95% confidence intervals, and test feature shifts.
