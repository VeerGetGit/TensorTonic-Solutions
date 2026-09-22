def gradient_descent_quadratic(a: float, b: float, c: float, x0: float, lr: float, steps: int) -> float:
    """
    Returns the final scalar x after the requested iterations.
    """
    # Write code here
    x=x0
    for _ in range(steps):
        gradient  = 2*a*x + b 
        x = x - lr*gradient
    return x

    """ In gradient descent the gradient is the derivative of the function which is multiplied by the learning rate alpha here it is lr and each parameter  x = x - lr*gradient is operated on this to optimize value"""