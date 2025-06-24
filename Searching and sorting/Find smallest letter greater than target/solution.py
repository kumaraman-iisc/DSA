def next_greatest_letter(letters, target):
    """
    Return the smallest character in letters that is lexicographically greater than target.

    Parameters:
    letters (List[char]): Sorted array of characters.
    target (char): The target character.

    Returns:
    char: The smallest character greater than target, or the first character if no such character exists.
    """
    # Implement the function logic
    left, right = 0, len(letters) - 1
    result = letters[0]
    
    while left <= right:
        mid = (left + right) // 2
        
        if letters[mid] > target:
            result = letters[mid]
            right = mid - 1
            
        else:
            left = mid + 1
            
    return result
    
    pass
