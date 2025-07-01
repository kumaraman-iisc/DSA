def can_be_rotated(mat, target):
    """
    Function to check if mat can be rotated to match target.
    :param mat: List[List[int]] -> The original matrix
    :param target: List[List[int]] -> The target matrix
    :return: bool -> True if mat can be rotated to match target, otherwise False
    """
    # TODO: Implement this function
    n = len(mat)
    
    def rotate(matrix):
        return [[matrix[n-j-1][i] for j in range(n)]for i in range(n)]
                
    for _ in range(4):
        if mat == target:
            return True
        mat = rotate(mat)
    return False
