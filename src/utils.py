"""Utility functions for EconoCausal data science workflows."""

from pathlib import Path
from typing import Tuple
import numpy as np
import pandas as pd


def load_hillstrom_dataset(data_path: str = "data/raw/hillstrom.csv") -> pd.DataFrame:
    """Load and preprocess the Kevin Hillstrom Email Analytics dataset."""
    path = Path(data_path)
    if not path.exists():
        path = Path("../data/raw/hillstrom.csv")
    if not path.exists():
        path = Path("data/fixtures/hillstrom_fixture.csv")
    if not path.exists():
        path = Path("../data/fixtures/hillstrom_fixture.csv")

    df = pd.read_csv(path)
    df["treatment"] = (df["segment"] != "No E-Mail").astype(int)
    df["mens_treatment"] = (df["segment"] == "Mens E-Mail").astype(int)
    df["womens_treatment"] = (df["segment"] == "Womens E-Mail").astype(int)
    df["outcome"] = df["conversion"].astype(int)
    return df


def generate_synthetic_pricing_data(
    n_samples: int = 2500, random_seed: int = 42
) -> Tuple[pd.DataFrame, float]:
    """Generate semi-synthetic customer pricing data with known ground-truth treatment effects."""
    rng = np.random.default_rng(random_seed)
    recency = rng.exponential(scale=6.0, size=n_samples).clip(1.0, 36.0)
    history = rng.lognormal(mean=4.8, sigma=0.8, size=n_samples).clip(10.0, 1500.0)
    frequency = rng.poisson(lam=2.5, size=n_samples).clip(1, 12)
    loyalty = rng.beta(a=2.0, b=3.0, size=n_samples)
    channel_web = rng.binomial(n=1, p=0.6, size=n_samples)

    # Confounded treatment propensity
    linear_score = (
        -0.8
        + 0.04 * recency
        - 0.0008 * history
        + 0.25 * loyalty
        + 0.3 * channel_web
    )
    propensity = 1.0 / (1.0 + np.exp(-linear_score))
    propensity = np.clip(propensity, 0.05, 0.95)
    treatment = rng.binomial(n=1, p=propensity)

    # Heterogeneous treatment effect: higher for loyal web customers
    true_ite = (
        0.05
        + 0.08 * loyalty
        + 0.03 * channel_web
        - 0.002 * (recency - 6.0)
    )
    baseline_y0 = 0.08 + 0.04 * loyalty + 0.02 * (frequency > 2)
    prob_conversion = np.clip(baseline_y0 + treatment * true_ite, 0.01, 0.99)
    conversion = rng.binomial(n=1, p=prob_conversion)

    df = pd.DataFrame({
        "customer_id": [f"cust_{i:05d}" for i in range(n_samples)],
        "recency": np.round(recency, 1),
        "history": np.round(history, 2),
        "frequency": frequency,
        "loyalty": np.round(loyalty, 3),
        "channel_web": channel_web,
        "treatment": treatment,
        "conversion": conversion,
        "true_ite": np.round(true_ite, 4),
    })
    true_ate = float(np.mean(true_ite))
    return df, true_ate
