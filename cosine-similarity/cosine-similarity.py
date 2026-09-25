import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    # Write code here
    a = np.asarray(a)
    b = np.asarray(b)

    norm_a = np.linalg.norm(a) #√(3²+4²)
    norm_b = np.linalg.norm(b)
    
    if(norm_a == 0.0 or norm_b == 0):
        return 0.0
    else:
        cosine  = (np.dot(a,b))/(norm_a*norm_b)
        
    return float(cosine)
    
    """
    v = np.array([3, -4])

    np.linalg.norm(v)        # L2 (default) → 5.0      √(3²+4²)
    np.linalg.norm(v, ord=1) # L1           → 7.0      |3|+|-4|
    np.linalg.norm(v, ord=np.inf) # L∞      → 4.0      max(|3|,|-4|)

    
    """