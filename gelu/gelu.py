import math
import numpy as np

def gelu(x: list) -> np.ndarray:
    """
    Returns a NumPy array with the same shape as x.
    """
    # Write code here
    x = np.asarray(x , dtype=float)
    erf_vector = np.vectorize(math.erf)
    gelu = x * 0.5 * (1+ erf_vector(x/(np.sqrt(2))))
    return (gelu)
    pass