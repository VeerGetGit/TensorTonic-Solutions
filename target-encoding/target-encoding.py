def target_encoding(categories: list, targets: list) -> list:
    """
    Returns each category replaced by its mean target.
    """
    # Write code here
    Output={}
    new_cat=categories
    new_cat=list(set(new_cat))
    for i in range(len(new_cat)):
        sum=0
        count=0
        for j in range(len(categories)):
            if(new_cat[i]==categories[j]):
               sum  = sum + targets[j]
               count +=1
            
        Output[new_cat[i]] = sum/count
  
    return [Output[cat] for cat in categories]   

    
    """
    encoding = {"a": 2.0, "b": 2.0, "c": 4.0}

    [encoding[cat] for cat in categories]

    categories = ["a",  "b",  "a",  "c" ]
               → [2.0,  2.0,  2.0,  4.0 ]
           
    """