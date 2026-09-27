import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    # Write code here
    x = np.asarray(x)
    n = x.size
    x_mean = np.mean(x)

    vari=(np.sum((x-x_mean)**2))/ (n-1)
    std = np.sqrt(vari)

    return {"variance":float(vari),"standard_deviation":float(std)}