def are_equal_strings(s, t):
    """
    Function to check if two strings are equal without using built-in functions.
    
    Parameters:
    s (str): The first string.
    t (str): The second string.
    
    Returns:
    bool: True if the strings are equal, False otherwise.
    """
    # Your code here
    len_s = len(s)
    len_t = len(t)
    
    if len_s != len_t:
        return False
    
    for i in range(len_s):
        for j in range(len_t):
            if len_s==len_t and s[i] == t[j]:
                return True
                
            else:
                return False
                
    return True
