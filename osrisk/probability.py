import numpy as np
from scipy import stats
from dataclasses import dataclass
from typing import Any, Dict, List, Optional

class Distribution:
    """Base class for a probability distribution."""
    def sample(self, random_state: Optional[np.random.Generator] = None) -> float:
        raise NotImplementedError

@dataclass
class FixedValue(Distribution):
    value: float

    def sample(self, random_state: Optional[np.random.Generator] = None) -> float:
        return float(self.value)

@dataclass
class NormalDistribution(Distribution):
    mean: float
    std: float

    def sample(self, random_state: Optional[np.random.Generator] = None) -> float:
        rng = random_state or np.random.default_rng()
        return float(rng.normal(self.mean, self.std))

@dataclass
class WeibullDistribution(Distribution):
    shape: float
    scale: float

    def sample(self, random_state: Optional[np.random.Generator] = None) -> float:
        rng = random_state or np.random.default_rng()
        return float(stats.weibull_min(c=self.shape, scale=self.scale).rvs(random_state=rng))


@dataclass
class UniformDistribution(Distribution):
    low: float
    high: float

    def sample(self, random_state: Optional[np.random.Generator] = None) -> float:
        rng = random_state or np.random.default_rng()
        return float(rng.uniform(self.low, self.high))


@dataclass
class TriangularDistribution(Distribution):
    left: float
    mode: float
    right: float

    def sample(self, random_state: Optional[np.random.Generator] = None) -> float:
        rng = random_state or np.random.default_rng()
        return float(rng.triangular(self.left, self.mode, self.right))


@dataclass
class LogNormalDistribution(Distribution):
    mean: float
    sigma: float

    def sample(self, random_state: Optional[np.random.Generator] = None) -> float:
        rng = random_state or np.random.default_rng()
        return float(rng.lognormal(self.mean, self.sigma))


@dataclass
class ExponentialDistribution(Distribution):
    scale: float

    def sample(self, random_state: Optional[np.random.Generator] = None) -> float:
        rng = random_state or np.random.default_rng()
        return float(rng.exponential(self.scale))


@dataclass
class GammaDistribution(Distribution):
    shape: float
    scale: float

    def sample(self, random_state: Optional[np.random.Generator] = None) -> float:
        rng = random_state or np.random.default_rng()
        return float(rng.gamma(self.shape, self.scale))


@dataclass
class BetaDistribution(Distribution):
    alpha: float
    beta: float

    def sample(self, random_state: Optional[np.random.Generator] = None) -> float:
        rng = random_state or np.random.default_rng()
        return float(rng.beta(self.alpha, self.beta))


@dataclass
class PoissonDistribution(Distribution):
    lam: float

    def sample(self, random_state: Optional[np.random.Generator] = None) -> float:
        rng = random_state or np.random.default_rng()
        return float(rng.poisson(self.lam))


@dataclass
class DiscreteDistribution(Distribution):
    values: List[float]
    probs: List[float]

    def sample(self, random_state: Optional[np.random.Generator] = None) -> float:
        rng = random_state or np.random.default_rng()
        return float(rng.choice(self.values, p=self.probs))


def from_spec(spec: Any) -> Distribution:
    """Create a distribution from a specification.

    The spec can be:
        - a number -> FixedValue
        - a dict with a 'type' key specifying the distribution
    """
    if isinstance(spec, (int, float)):
        return FixedValue(value=float(spec))
    if not isinstance(spec, Dict):
        raise ValueError("Invalid distribution specification: %r" % spec)
    dtype = spec.get('type')
    if dtype == 'fixed':
        return FixedValue(value=float(spec['value']))
    if dtype == 'uniform':
        return UniformDistribution(low=spec['low'], high=spec['high'])
    if dtype == 'triangular':
        return TriangularDistribution(left=spec['left'], mode=spec['mode'], right=spec['right'])
    if dtype == 'normal':
        return NormalDistribution(mean=spec['mean'], std=spec['std'])
    if dtype == 'lognormal':
        return LogNormalDistribution(mean=spec['mean'], sigma=spec['sigma'])
    if dtype == 'exponential':
        return ExponentialDistribution(scale=spec['scale'])
    if dtype == 'weibull':
        return WeibullDistribution(shape=spec['shape'], scale=spec['scale'])
    if dtype == 'gamma':
        return GammaDistribution(shape=spec['shape'], scale=spec['scale'])
    if dtype == 'beta':
        return BetaDistribution(alpha=spec['alpha'], beta=spec['beta'])
    if dtype == 'poisson':
        return PoissonDistribution(lam=spec['lam'])
    if dtype == 'discrete':
        return DiscreteDistribution(values=spec['values'], probs=spec['probs'])
    raise ValueError(f"Unknown distribution type: {dtype}")
