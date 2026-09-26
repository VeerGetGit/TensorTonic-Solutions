import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    # Write code here
    a = np.asarray(A)
    rows , cols  = a.shape
    results = np.empty((cols, rows)) 
    
    """
    The np.empty() function in NumPy is used to create a new array of a specified shape       and type without initializing the entries. This means the array will contain 
    arbitraryvalues.
    
    """
    for i in range(rows):
        for j in range(cols):
            results[j][i]=a[i][j]
    
    return results

    """
    simple two line soln:
    a = np.asarray(A)
    a.T
    """