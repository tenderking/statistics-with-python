import numpy as np
from scipy.stats import f
from .manova import manova

def test_manova():
   
    # Test case 5
    n_samples = 100  # Increase sample size compared to the original test case
    n_features = 3

    # Generate random data with slight variations
    X = np.random.rand(n_samples, n_features) * 0.5 + 0.25
    Y = X + np.random.randn(n_samples, n_features) * 20
    t_squared, c_squared = manova(X, Y)
    assert t_squared >= 0, "T-squared statistic should be non-negative"
    assert 0 <= c_squared <= 1, "P-value (c-squared) should be between 0 and 1"

    print("All tests pass!")

if __name__ == '__main__':
    test_manova()