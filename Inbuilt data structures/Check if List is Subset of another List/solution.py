def is_subset(lst1, lst2):
    # Your code goes here
    for element in lst1:
        found = False
        
        for item in lst2:
            if item == element:
                found = True
                break
            
        if not found:
            return False
        
    return True
    pass
