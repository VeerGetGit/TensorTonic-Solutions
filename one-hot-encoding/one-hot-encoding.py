import numpy as np

def one_hot(y: list, num_classes=None) -> np.ndarray:
    """
    Returns a NumPy array with shape (N, K).
    """
    
    # Write code here
    y = np.asarray(y)
    N = len(y)
    
    if num_classes is None:
        num_classes = max(y)+1

    Output = np.zeros((N,num_classes))

    Output[np.arange(N),y]=1

    return Output
    
    
    pass