def bubble_sort(lst):
    # Your code goes here
    size = len(lst)
    
    for i in range(size):
        for j in range(0, size-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
            
    return lst
    pass
