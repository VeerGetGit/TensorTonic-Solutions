import numpy as np

def expected_value_discrete(x: list, p: list) -> float:
    """
    Returns the expected value as a Python float.
    """
    # Write code here
    x = np.asarray(x, dtype=float)
    p = np.asarray(p, dtype =float)

    expect_value = np.sum(x*p)
    return expect_value
    