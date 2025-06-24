def countNegatives(grid):
    # Implement your solution here
    count = 0
    
    for lst in grid:
        for item in lst:
            if item < 0:
                count += 1
            
    return count
                    
    pass
