import numpy as np

def bernoulli_pmf_and_moments(x: list, p: float) -> dict:
    """
    Returns a dictionary with pmf, mean, and variance.
    """
    # Write code here

    x  = np.asarray(x, dtype = float)
    mean  = float(p)
    variance = float(p*(1-p))

    pmf = np.empty_like(x)
    
    for i in range(x.size):
        if x.flat[i] == 0:
            pmf.flat[i] = 1 - p
        elif(x.flat[i]==1):
            pmf.flat[i] = p

    return {"pmf":pmf,"mean":mean,"variance":variance}