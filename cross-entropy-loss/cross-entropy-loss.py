import numpy as np

def cross_entropy_loss(y_true: list[int], y_pred: list[list[float]]) -> float:
    """
    Returns the mean multiclass cross-entropy loss as a Python float.
    """
    # Write code here
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred , dtype = float)

    N  = len(y_true)
    
    row_indices = np.arange(N)

    correct_probab = y_pred[row_indices,y_true]

    Output  = -(np.mean(np.log(correct_probab)))

    return Output
    """
     y_pred[[rows], [cols]]
           ↑         ↑
       paired    paired
       together  together
    
    
       y_true = [2, 0, 1]   # different correct classes
    
    y_pred[[0,1,2], [2,0,1]]
    
    row index → [0,  1,  2]
    col index → [2,  0,  1]
                  ↓   ↓   ↓
               [0,2][1,0][2,1]
    
    y_pred[0][2] = 0.05
    y_pred[1][0] = 0.1
    y_pred[2][1] = 0.2
    
    → [0.05, 0.1, 0.2]
    
    
     """