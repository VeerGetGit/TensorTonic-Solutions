import numpy as np

def pearson_correlation(X: list) -> np.ndarray:
    """
    Returns the correlation matrix as a NumPy array.
    """
    # Write code here
    X = np.asarray(X, dtype =float)
    mean = np.mean(X, axis=0) #axis=0 means along the column
    X_center = X-mean
    N = X.shape[0]

    covar = (X_center.T @ X_center)/(N-1)

    std = np.sqrt(np.diag(covar))
    corr = covar / np.outer(std,std)
    return corr
    
    """
    The diagonal always holds the variance of each feature:
    covar[0,0] = variance of col0
    covar[1,1] = variance of col1

    np.diag(covar) = [1.0, 9.333]   ← [var of col0, var of col1]
    np.sqrt(np.diag(covar)) = [1.0, 3.055]  ← [std of col0, std of col1]

    np.outer(a, b) builds a matrix where every element is a[i] × b[j]:
    a = [1.0, 3.055]
    b = [1.0, 3.055]

    np.outer(a, b):
    
             b[0]=1.0    b[1]=3.055
    a[0]=1.0  [1.0×1.0,  1.0×3.055]   =  [1.0,   3.055]
    a[1]=3.055 [3.055×1.0, 3.055×3.055] =  [3.055, 9.333]

    So, outer[i,j] = std[i] × std[j]

    Why we need outer
    The Pearson formula divides by std_x × std_y for each pair:
    r[0,1] = covar[0,1] / (std[0] × std[1])
    r[1,0] = covar[1,0] / (std[1] × std[0])
    r[0,0] = covar[0,0] / (std[0] × std[0])
    r[1,1] = covar[1,1] / (std[1] × std[1])

    np.outer builds exactly that denominator matrix in one shot:
    outer = [[std[0]×std[0],  std[0]×std[1]],
         [std[1]×std[0],  std[1]×std[1]]]

      = [[1.0,   3.055],
         [3.055, 9.333]]
         

    corr = covar / outer

    [0,0]: 1.0   / 1.0   = 1.0     ← col0 vs col0
    [0,1]: -2.0  / 3.055 = -0.655  ← col0 vs col1
    [1,0]: -2.0  / 3.055 = -0.655  ← col1 vs col0
    [1,1]: 9.333 / 9.333 = 1.0     ← col1 vs col1

    Simple analogy for outer
    Think of it like a multiplication table:
              1    2    3
    1  [1×1, 1×2, 1×3]   = [1, 2, 3]
    2  [2×1, 2×2, 2×3]   = [2, 4, 6]
    3  [3×1, 3×2, 3×3]   = [3, 6, 9]

    np.outer() <-- It takes 1D matrix to solve like table and remember if you try to 
                       pass 2D matrix in np.outer() it flattens into 1D and solve that to
                       get answers.
    """