def longest_word_length(s):
    """
    Function to find the length of the longest word in a string without using built-in functions.
    """
    length = 0
    words = s.split()
    
    for word in words:
        if len(word) > length:
            length = len(word)
    
    return length
