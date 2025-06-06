"""Demonstration of using probability distributions in a Monte Carlo loop."""
from osrisk import from_spec
import numpy as np

# Example of using distributions in place of numbers
params = {
    "duration": {"type": "weibull", "shape": 1.5, "scale": 10.0},
    "cost": {"type": "normal", "mean": 1000.0, "std": 100.0},
    "downtime_factor": {"type": "uniform", "low": 0.8, "high": 1.2},
}

# Convert parameter specifications to distribution objects
for key, spec in params.items():
    params[key] = from_spec(spec)

# Simple Monte Carlo simulation
N = 1000
results = []

rng = np.random.default_rng()
for _ in range(N):
    duration = params["duration"].sample(rng)
    cost = params["cost"].sample(rng)
    downtime_factor = params["downtime_factor"].sample(rng)
    results.append(duration * cost * downtime_factor)

print(f"Simulated {N} trials. Mean outcome: {np.mean(results):.2f}")
