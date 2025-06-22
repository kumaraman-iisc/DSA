def linear_search(arr, target):
    # TODO: Implement this function
    size = len(arr)
    
    for index in range(0, size):
        if arr[index] == target:
            return index
            
    return -1
    pass
