import numpy as np
from scipy.stats import f
def manova(X, Y):
    """Performs a multivariate analysis of variance (MANOVA) on the given data.

    Args:
    X (numpy.ndarray): A 2D array of shape (n, p) where n is the number of samples and p is the number of variables.
    Y (numpy.ndarray): A 2D array of shape (n, q) where n is the number of samples and q is the number of response variables.

    Returns:
    float: The F-statistic for the MANOVA.
    float: The p-value for the MANOVA.
    """
    X_mat = X.values
    Y_mat = Y.values
    n1, p1 = X_mat.shape
    n2, p2 = Y_mat.shape
    n = n1 + n2
    p = p1
    s_1 = np.cov(X_mat, rowvar=False)
    s_2 = np.cov(Y_mat, rowvar=False)
    s_pooled = (n1-1)/n * s_1+ (n2-1 )/n * s_2
    mu_1 = np.mean(X_mat, axis=0) # Reshape to column vector
    mu_2 = np.mean(Y_mat, axis=0)  # Reshape to column vector
    mu_diff = mu_1 - mu_2
    print("mu_1: ",mu_1.shape)
    print("mu_1: ",mu_1)
    print("mu_2: ",mu_2)
    print("mu_2: ",mu_2.shape)
    print("mu_diff: ",mu_diff)
    print("mu_diff: ",mu_diff.shape)
    print("s_pooled: ",s_pooled.shape)
    print("s_1: ",s_1.shape)
    print("s_2: ",s_2.shape)
    print("X: ",X_mat.shape)
    print("Y: ",Y_mat.shape)
    t_squared = mu_diff.T @ np.linalg.inv((1/n1+1/n2)*s_pooled) @ mu_diff
    c_squared = (n1+n2-2)*(p-1)/(n-p)*f.ppf(0.95, p-1, n-p)
    return t_squared, c_squared