import numpy as np

def kl_divergence(p: list, q: list, eps: float = 1e-12) -> float:
    """
    Returns the divergence as a float.
    """
    # Write code here
    q = np.asarray(q , dtype = float)
    p = np.asarray(p , dtype = float)

    positive = p>0

    q_safe = np.clip(q[positive],eps,None)

    Output = np.sum(p[positive] * (np.log(p[positive]/q_safe)))

    return float(Output)
    