import math

def poisson_pmf_cdf(lam: float, k: int) -> dict:
    """
    Returns a dictionary with pmf and cdf.
    """
    # Write code here
    pmf = ((lam ** k) * math.exp(-lam)) / (math.factorial(k))

    cdf = 0
    for i in range(k+1):
        cdf = cdf + ((lam ** i) * math.exp(-lam)) / (math.factorial(i))

    return {"pmf":pmf,"cdf": cdf}
        