import numpy as np

def tanh(x: list) -> np.ndarray:
    """
    Returns a NumPy array with the same shape as x.
    """
    # Write code here
    x = np.asarray(x, dtype =float)
    tan_sol = np.tanh(x)

    return tan_sol

    # OR
    # return (np.exp(x) - np.exp(-x)) / (np.exp(x) + np.exp(-x))

    
    pass