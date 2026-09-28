import numpy as np

def covariance_matrix(X: list) -> np.ndarray:
    """
    Returns the covariance matrix as a NumPy array.
    """
    # Write code here
    X = np.asarray(X, dtype=float)
    mean = np.mean(X, axis=0)
    X_c = X-mean
    N = X.shape[0]  #len(X)

    sigma = (X_c.T @ X_c)/(N-1)
    return sigma

    """
    
    @ <-- this gives proper and do proper matrix multiplication
    X_c <-- this is centered matrix and the mean should also be matrix but in the column 
    wise.
    x.shape <-- it return the shape of matrix
    but x.shape[0]<-- it tells no of rows like this len(x) do.
    x.shape[1]<-- gives no of columns in a matrix.
    len(x)<-- this returns the no of rows in a matrix.
    
    
    """