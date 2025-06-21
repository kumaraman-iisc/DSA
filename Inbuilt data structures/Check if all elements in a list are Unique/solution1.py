def check_unique(lst):
    # Your code goes here
    for i in range(len(lst)):
        for j in range(i):
            if lst[i] == lst[j]:
                return False
            
    return True
    pass
