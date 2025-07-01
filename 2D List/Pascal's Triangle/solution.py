def generate(numRows):
    """
    Function to generate the first numRows of Pascal's triangle.
    :param numRows: int -> Number of rows of Pascal's triangle to generate
    :return: List[List[int]] -> The first numRows of Pascal's triangle
    """
    # TODO: Implement this function
    res = [[1]]
    
    if numRows == 0:
        return []
        
    elif numRows == 1:
        return [[1]]
    
    for _ in range(numRows - 1):
        rows = []
        dummy = [0] + res[-1] + [0]
        
        for i in range(len(res[-1]) + 1):
            rows.append(dummy[i] + dummy[i+1])
        res.append(rows)
        
    return res
