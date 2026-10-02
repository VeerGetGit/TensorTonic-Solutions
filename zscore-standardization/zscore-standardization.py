import numpy as np

def zscore_standardize(X: list, axis: int = 0, eps: float = 1e-12) -> np.ndarray:
    """
    Returns population Z-scores as a NumPy array matching the shape of X.
    """
    # Write code here
    x =  np.asarray(X, dtype=float)

    mean = np.mean(x, axis=axis, keepdims=True)
    std = np.std(x, axis=axis,keepdims = True)
    std = np.where(std>eps,std,1.0)
    z_score = (x - mean)/(std)

    return z_score
    
    """
    axis helps to create mean along the row and column
    and
    keepdims maintains the shape which is imp while subtracting to retain the shape
    of matrix
    """