import numpy as np

def nesterov_momentum_step(w: list, v: list, grad: list, lr: float = 0.01, momentum: float = 0.9) -> dict:
    """
    Returns a dictionary with new_w and new_v.
    """
    # Write code here
    w = np.asarray(w)
    v = np.asarray(v)
    grad = np.asarray(grad)

    complete_new_v = momentum * v + lr * grad
    new_weight = w - complete_new_v

    return {"new_w": new_weight , "new_v":complete_new_v}
    pass