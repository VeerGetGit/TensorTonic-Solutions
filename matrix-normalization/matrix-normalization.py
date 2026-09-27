import numpy as np

def matrix_normalization(matrix: list, axis=None, norm_type: str = "l2") -> np.ndarray:
    """
    Returns a NumPy array with the same shape as matrix.
    """
    # Write code here
    """
    v = np.array([3, -4])
    np.linalg.norm(v, ord=None)        # L2 (default) → 5.0      √(3²+4²)
    np.linalg.norm(v, ord=1) # L1           → 7.0      |3|+|-4|
    np.linalg.norm(v, ord=np.inf) # L∞      → 4.0      max(|3|,|-4|)

    Norm	       Formula	        Meaning
    L2 (default)	√(Σx²)	         Straight-line distance
    L1	             Σ|x|	         Sum of absolute values
    L∞	             max(|x|)	     Largest absolute value
    
    """
    matrix  = np.asarray(matrix, dtype = float)

    if norm_type == "l1":
         norm = np.linalg.norm(matrix, ord=1 , axis = axis ,keepdims =True) 
        #these create norm vectors which needs to divide the original matrix to get 
        # normalized matrix
    elif norm_type == "l2":
        norm = np.linalg.norm(matrix , ord=None, axis = axis , keepdims =True)
    elif norm_type == "max":
        norm = np.linalg.norm(matrix, ord=np.inf , axis=axis , keepdims =True)

    norm = np.where(norm == 0 , 1.0 , norm)
    return matrix/norm


    """
    because if norm has 0 and if element inside matrix get divide by 0 present in norm
    then it will crash or give nan. that is why replacing norm wherever is zero with 1
    so that if 0 gets divide by 1 then it will be 1.

    ##### np.where(condition, value_if_true, value_if_false)

    #####np.where(norm == 0, 1.0, norm)
    # for each element:
    #   if norm == 0 → use 1.0
    #   else         → use norm

    matrix = [[0, 0, 0],
          [1, 2, 2]]

    # L2 norm of row 0:
    # √(0² + 0² + 0²) = √0 = 0
    
    norm = [[0.],    ← uh oh!
            [3.]]
    
    matrix / norm = [[0/0, 0/0, 0/0],   ← division by zero!
                     [1/3, 2/3, 2/3]]

    [[nan, nan, nan],    ← nan = "not a number"
     [0.333, 0.666, 0.666]]

    #####so if we replaced 0 with 1 then:

     norm = [[1.],    ← replaced 0 with 1.0
        [3.]]

    matrix / norm = [[0/1, 0/1, 0/1],   ← stays [0, 0, 0] ✓
                     [1/3, 2/3, 2/3]]
    """