def count_words(s):
    """
    Function to count the number of words in the input string.
    
    Parameters:
    s (str): The input string to check for words.
    
    Returns:
    int: The count of words in the input string.
    """
    # Your code here
    words = s.split()
    count = 0
    
    for word in words:
        count += 1
        
    return count
