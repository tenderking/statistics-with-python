import numpy as np


def estimated_minimum_ecm(df1, df2):
    """
    Estimate the minimum Expected Classification Error (ECM) between two dataframes.
    Assumes that the covariance matrices are the same.
    """
    # Get the dimensions of the dataframes
    n1, p = df1.shape
    n2, _ = df2.shape
    
    # Print dataframe dimensions for reference
    print(f"Dataframe 1: n={n1}, p={p}")
    print(f"Dataframe 2: n={n2}, p={p}")
    
    # Calculate means and covariance matrices
    df1_mean = df1.mean()
    df2_mean = df2.mean()
    df1_cov = np.cov(df1.T)
    df2_cov = np.cov(df2.T)
    
    # Calculate the pooled covariance matrix
    S_pooled = ((n1 - 1) * df1_cov + (n2 - 1) * df2_cov) / (n1 + n2 - 2)
    
    # Calculate the difference and sum of means
    mu_diff = df1_mean - df2_mean
    mu_sum = df1_mean + df2_mean
    
    # Estimate parameters for the decision boundary
    m_hat = 0.5 * mu_diff @ np.linalg.inv(S_pooled) @ mu_sum
    a_hat = np.linalg.inv(S_pooled) @ mu_diff
    
    # Initialize counters for errors in each dataframe
    count_1, count_2 = 0, 0
    
    # Calculate errors for dataframe 1
    for i in range(n1):
        dist = df1.iloc[i] @ a_hat - m_hat
        if dist > 0:
            count_1 += 1
    
    # Calculate errors for dataframe 2
    for i in range(n2):
        dist = df2.iloc[i] @ a_hat - m_hat
        if dist > 0:
            count_2 += 1
    
    # Calculate and print the overall error rate
    error_rate = 1 - (count_1 + count_2) / (n1 + n2)
    print(f"Overall Error Rate: {error_rate}")
    
    return error_rate, m_hat, a_hat

# Example usage:
# error, m_hat, a_hat = estimated_minimum_ecm(df1, df2)
