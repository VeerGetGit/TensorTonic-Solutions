from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    # Write code here
    x = np.asarray(x)
    m = np.mean(x)
    med = np.median(x)

    freq = {}
    for val in x:
        freq[val] = freq.get(val,0)+1

    mod = max(freq , key= lambda k : freq[k]) 
    
    """key= — tells max what to compare by
           key is a function that max applies to each element before comparing:"""
    
    return {"mean":float(m),"median":float(med),"mode":float(mod)}
   
    """
    x = np.asarray(x)
    m   = np.mean(x)
    med = np.median(x)
    mod = Counter(x).most_common(1)[0][0]

    return {"mean": m, "median": med, "mode": mod}
        
    """

    """
    ## How `freq.get(val, 0) + 1` Works

    ---
    
    ## `dict.get(key, default)`
    
    `.get()` is a safe way to read from a dictionary:
    - If the key **exists** → returns its value
    - If the key **doesn't exist** → returns the `default` instead of crashing
    
    ```python
    freq = {1: 2}
    
    freq.get(1, 0)   # → 2   (key exists, return its value)
    freq.get(5, 0)   # → 0   (key doesn't exist, return default 0)
    ```
    
    Without `.get()` you'd get a crash:
    ```python
    freq[5]   # ❌ KeyError: 5
    ```
    
    ---
    
    ## The Full Line
    
    ```python
    freq[val] = freq.get(val, 0) + 1
    ```
    
    Means:
    > *"Get the current count of `val` (or 0 if not seen yet), then add 1 to it"*
    
    ---
    
    ## Trace Through Example
    
    ```python
    x = [1, 1, 2, 3]
    freq = {}
    
    val=1 → freq.get(1, 0) = 0  → freq[1] = 0+1 = 1   → freq={1:1}
    val=1 → freq.get(1, 0) = 1  → freq[1] = 1+1 = 2   → freq={1:2}
    val=2 → freq.get(2, 0) = 0  → freq[2] = 0+1 = 1   → freq={1:2, 2:1}
    val=3 → freq.get(3, 0) = 0  → freq[3] = 0+1 = 1   → freq={1:2, 2:1, 3:1}
    ```
    
    First time a value is seen → starts at 0, becomes 1.
    Every repeat → count goes up by 1.
        """

    """
        Good question!
    
    `.most_common(n)` returns the **top n most frequent elements**.
    
    ```python
    Counter([1, 1, 2, 3]).most_common(1)  # → [(1, 2)]         ← top 1
    Counter([1, 1, 2, 3]).most_common(2)  # → [(1, 2), (2, 1)] ← top 2
    Counter([1, 1, 2, 3]).most_common(3)  # → [(1, 2), (2, 1), (3, 1)] ← top 3
    ```
    
    We only use `1` because we only want **one mode** — the single most frequent element.
    
    If you used `2` you'd get a list of 2 tuples, and you'd still need to pick the first one anyway:
    
    ```python
    .most_common(2)[0][0]   # still gives 1 — same result, extra data
    .most_common(1)[0][0]   # gives 1 — cleaner, only fetches what we need
    ```
    
    ---
    
    The only time you'd want `2` or more is if you're looking for **multiple modes**:
    
    ```python
    # x = [1, 1, 2, 2, 3]  ← two modes: 1 and 2
    Counter(x).most_common(2)        # → [(1,2), (2,2)]
    [v for v,c in Counter(x).most_common(2)]  # → [1, 2]
    ```
    
    But for a single mode, `1` is always enough.
    """

    """
    
    """