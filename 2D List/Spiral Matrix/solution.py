def spiral_order(matrix):
    """
    Function to return the elements of the matrix in spiral order.
    :param matrix: List[List[int]] -> The input matrix
    :return: List[int] -> The elements in spiral order
    """
    # TODO: Implement this function
    rows, cols = len(matrix), len(matrix[0])
    res = []
    x, y, dx, dy = 0, 0, 1, 0
    
    for _ in range(rows * cols):
        res.append(matrix[y][x])
        matrix[y][x] = "*"
        
        if not 0 <= x + dx < cols or not 0 <= y + dy < rows or matrix[y+dy][x+dx] == "*":
            dx, dy = -dy, dx
        x += dx
        y += dy
    
    return res
