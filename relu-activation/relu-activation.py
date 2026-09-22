import numpy as np

def relu(x) -> np.ndarray:
    """
    Returns a NumPy array with the same shape as x.
    """

    """
    steps to solve this:
    1) first i have converted x as array.
    2) then i have created the result array similar to x array 
    using empty_like(Same shape, uninitialized (fastest, since it skips filling))
    3) i have run the loop of x.size
    4) then i store the value using np.maximum(0,x.flat[i]) as relu is max(o,x)
     in result array.
    5) i have used flat because 
    .flat is a flat iterator — it lets you treat any array as if it's a 1D 
    list,regardless of the shape.
    
        How .flat sees the 2D array
        .flat reads the array row by row (left to right, top to bottom):
        
        x = [[1, 2],
             [3, 4]]
        
        x.flat[0] → 1
        x.flat[1] → 2
        x.flat[2] → 3
        x.flat[3] → 4
        Loop trace
        i=0 → result.flat[0] = max(0.0, 1) = 1
        i=1 → result.flat[1] = max(0.0, 2) = 2
        i=2 → result.flat[2] = max(0.0, 3) = 3
        i=3 → result.flat[3] = max(0.0, 4) = 4

        flat helps us to reduce the concept of [][] 2d indexing 
        where first i need to fo rows for one loop and inside that loop another loop 
        column
        like this:
        for i in range(rows):
            for j in range(cols):
                result[i][j] = max(0.0, x[i][j])  # double indexing
    """
   # Write code here
    x = np.array(x) 
    results = np.empty_like(x)
    for i in range(x.size):
        results.flat[i] = np.maximum(0,x.flat[i])

    return results

    
    