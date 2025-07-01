def search_matrix(matrix, target):
    """
    Function to search for a target in the matrix.
    :param matrix: List[List[int]] -> The input matrix
    :param target: int -> The target value to search for
    :return: bool -> True if target is found, False otherwise
    """
    # TODO: Implement this function
    if not matrix or not matrix[0]:
        return False
        
    rows = len(matrix)
    cols = len(matrix[0])
    
    low, high = 0, rows*cols - 1
    
    while low <= high:
        mid = (low + high) // 2
        row = mid // cols
        col = mid % cols
        
        mid_value = matrix[row][col]
        
        if mid_value == target:
            return True
            
        elif mid_value < target:
            low = mid + 1
            
        else:
            high = mid - 1
            
    return False
