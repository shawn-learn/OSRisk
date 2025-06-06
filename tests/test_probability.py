import unittest
from osrisk import from_spec, FixedValue

class TestProbability(unittest.TestCase):
    def test_fixed_value(self):
        dist = from_spec(5)
        self.assertIsInstance(dist, FixedValue)
        self.assertEqual(dist.sample(), 5.0)

    def test_normal_distribution(self):
        dist = from_spec({"type": "normal", "mean": 0, "std": 1})
        val = dist.sample()
        self.assertIsInstance(val, float)

    def test_weibull_distribution(self):
        dist = from_spec({"type": "weibull", "shape": 2.0, "scale": 3.0})
        val = dist.sample()
        self.assertIsInstance(val, float)

    def test_uniform_distribution(self):
        dist = from_spec({"type": "uniform", "low": 0.0, "high": 1.0})
        val = dist.sample()
        self.assertTrue(0.0 <= val <= 1.0)

    def test_discrete_distribution(self):
        dist = from_spec({"type": "discrete", "values": [1, 2], "probs": [0.3, 0.7]})
        val = dist.sample()
        self.assertIn(val, [1, 2])

if __name__ == "__main__":
    unittest.main()
