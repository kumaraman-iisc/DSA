def remove_duplicates(s):
    """
    Function to remove duplicate characters from the input string.
    
    Parameters:
    s (str): The input string from which duplicates need to be removed.
    
    Returns:
    str: The modified string with duplicates removed.
    """
    # Your code here
    unique = []
    
    for char in s:
        if char not in unique:
            unique.append(char)
        
    return ''.join(unique)
