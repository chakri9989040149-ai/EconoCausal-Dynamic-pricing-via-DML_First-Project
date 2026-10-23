# EconoCausal – Dynamic Pricing via Double Machine Learning

Welcome to my project journal for **EconoCausal**, a pure Data Science and Machine Learning project exploring causal inference, heterogeneous treatment effects, and budget-constrained price optimization.

---

## Day 1: Project Introduction, Objectives, Tools & Technologies, and Workflow

### 1. Project Introduction
EconoCausal is a Data Science and Machine Learning project focused on understanding how discounts and promotional pricing affect customer purchasing behaviour. Traditional machine learning models often rely on standard predictive correlations: they predict who is likely to buy, but fail to answer who will buy *specifically because of a discount*. 

By leveraging **Causal Inference** and **Double Machine Learning (DML)**, this project decouples confounding factors from true incremental treatment effects (uplift). It aims to answer not only what the causal effect of a price discount is on individual customers, but also how to optimally distribute promotions within a limited marketing budget to maximize net profit.

### 2. Objectives
- **Understand discount effects:** Investigate how promotional discount interventions impact customer conversion and spending patterns.
- **Analyse the discount-purchase relationship:** Explore empirical purchasing distributions and identify confounding variables that bias discount assignment.
- **Estimate true treatment effects:** Apply Causal Inference and Double Machine Learning (DML) with Neyman-orthogonal score equations to estimate Conditional Average Treatment Effects (CATE) free of nuisance model bias.
- **Allocate a limited discount budget:** Formulate and solve a constrained Multiple-Choice Knapsack optimization problem to distribute promotion tiers efficiently.
- **Support data-driven pricing decisions:** Provide actionable customer segmentation and counterfactual simulations to guide strategic business decisions.

### 3. Tools and Technologies
- **Programming Language:** Python
- **Data Manipulation & Numerics:** Pandas, NumPy, SciPy
- **Causal Inference & ML:** EconML (LinearDML, Causal Forest), DoWhy (SCM DAGs, refutation audits), Scikit-Learn
- **Exploration & Development:** Jupyter Notebook, JupyterLab
- **Data Visualisation:** Matplotlib, Plotly
- **Version Control:** Git and GitHub

*(This repository is strictly a data science project without any web dashboards, frontend frameworks, or deployment servers).*

### 4. Project Workflow
1. **Dataset Collection:** Ingest real-world RCT data (Kevin Hillstrom Email Analytics Challenge) and generate ground-truth semi-synthetic pricing data.
2. **Data Exploration:** Inspect distributions, calculate conversion and visit rates across campaign arms, and verify covariate balance using Standardized Mean Differences (SMD).
3. **Data Preprocessing:** Clean covariates, encode categorical variables, and format treatment indicators.
4. **Causal Analysis:** Define the Directed Acyclic Graph (DAG), verify common support / propensity score overlap, calculate Kish Effective Sample Size (ESS), and execute DoWhy falsification refuters.
5. **Double Machine Learning:** Train EconML `LinearDML` with cross-fitting to estimate individualized treatment effects and benchmark against S-Learner and T-Learner baselines.
6. **Budget Optimisation:** Segment customers into 4 quadrants (Persuadables, Sure Things, Lost Causes, Sleeping Dogs) and solve the Multiple-Choice Knapsack problem under budget caps.
7. **Data Visualisation:** Plot Love plots, propensity overlap, uplift curves, budget sensitivity curves, and confidence intervals.
8. **Results and Insights:** Synthesize empirical findings, identify budget inflection points, and document strategic pricing conclusions.

### 5. Expected Outcome
The expected outcome is a fully reproducible, self-contained causal inference workflow that demonstrates how causal machine learning outperforms traditional predictive targeting, preventing wasted spend on organic buyers (Sure Things) and preventing customer opt-outs (Sleeping Dogs), while achieving higher incremental profit under strict budget caps.

---

## 📂 Repository Structure

The repository structure reflects a clean data science setup:

```text
EconoCausal/
├── data/
│   ├── fixtures/
│   │   ├── hillstrom_fixture.csv
│   │   └── lalonde_fixture.csv
│   └── raw/
│       ├── hillstrom.csv
│       └── lalonde.csv
├── notebooks/
│   ├── 01_eda.ipynb
│   ├── 02_causal_graph.ipynb
│   ├── 03_estimators.ipynb
│   ├── 04_policy.ipynb
│   └── 05_whatif_simulation.ipynb
├── progress/
│   ├── day1_progress.md
│   ├── day2_progress.md
│   ├── day3_progress.md
│   ├── day4_progress.md
│   ├── day5_progress.md
│   ├── day6_progress.md
│   └── day7_progress.md
├── src/
│   └── utils.py
├── .gitignore
├── README.md
└── requirements.txt
```

---

## 🚀 How to Run

### 1. Set Up Environment
```bash
# Clone the repository
git clone https://github.com/your-username/econocausal.git
cd econocausal

# Create and activate virtual environment
python -m venv .venv

# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Open Notebooks
```bash
jupyter lab
```
Navigate to `notebooks/` and open each notebook. Every notebook is self-contained and pre-executed with complete outputs, tables, and charts.

---

## 📅 Daily Progress

Follow my day-by-day project logs in the [`progress/`](progress/) directory:

- [**Day 1: Project Setup & Environment Initialization**](progress/day1_progress.md) – Environment configuration, dependency installation, dataset download, and helper creation.
- [**Day 2: Exploratory Data Analysis & Causal Balance**](progress/day2_progress.md) – Conversion rates across arms, average spend, and Standardized Mean Differences (SMD) Love plot.
- [**Day 3: Structural Causal Model & Identification Refutations**](progress/day3_progress.md) – NetworkX DAG, common support overlap, Kish ESS, and DoWhy refutations (Placebo, Common Cause, Subset).
- [**Day 4: Double Machine Learning & Estimator Benchmarking**](progress/day4_progress.md) – EconML `LinearDML` training, PEHE and CATE correlation benchmarking against S/T-learners, and Cumulative Uplift curves.
- [**Day 5: Policy Optimization & Knapsack Budget Allocation**](progress/day5_progress.md) – 4-quadrant uplift segmentation, Multiple-Choice Knapsack solver, and budget sensitivity curve.
- [**Day 6: Counterfactual What-If Simulator & Uncertainty Bounds**](progress/day6_progress.md) – Persona simulations, 95% confidence intervals, and loyalty sensitivity response sweeps.
- [**Day 7: Results, Insights and Final Summary**](progress/day7_progress.md) – End-to-end synthesis, methodological audit, and strategic pricing takeaways.
