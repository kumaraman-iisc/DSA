def rotate_list(lst, k):
    # Your code goes here
    rotation = []
    
    if not lst:
        return []
        
    k = k % len(lst)
    
    for _ in range(k):
        element = lst.pop()
        lst.insert(0, element)
        
    return lst
    pass
