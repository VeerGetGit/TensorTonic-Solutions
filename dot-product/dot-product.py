import numpy as np

def dot_product(x: list, y: list) -> float:
    """
    Returns the dot product as a float.
    """
    # Write code here
    x = np.asarray(x)
    y = np.asarray(y)
    result = np.dot(x,y)
    return float(result)