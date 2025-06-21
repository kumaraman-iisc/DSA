def max_consecutive_difference(lst):
    # Your code goes here
    diff = 0
    
    if len(lst) < 2:
        return 0
       
    for i in range(len(lst)-1):
        abs_diff = abs(lst[i]-lst[i+1])
        if diff < abs_diff:
            diff = abs_diff
    
    return diff
    pass
