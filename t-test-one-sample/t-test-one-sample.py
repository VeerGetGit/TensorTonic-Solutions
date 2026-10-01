import numpy as np

def t_test_one_sample(x: list, mu0: float) -> float:
    """
    Returns the t-statistic as a float.
    """
    # Write code here
    x  = np.asarray(x , dtype=float)
    x_mean = np.mean(x)
    n = x.size
    sum = 0 
    
    for i in range(n):
        sum = sum + (x.flat[i] - x_mean)**2

    
    std_deviation = np.sqrt((1/(n-1))*sum)

    one_sample_t = (x_mean - mu0)/(std_deviation/np.sqrt(n))

    return float(one_sample_t)
    