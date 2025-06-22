def is_substring(s, t):
    """
    Function to check if string t is a substring of string s without using built-in functions and recursion.
    
    Parameters:
    s (str): The main string.
    t (str): The string to check as a substring.
    
    Returns:
    bool: True if t is a substring of s, False otherwise.
    """
    # Your code here
    if len(t) == 0:
        return True
    
    substring = s.split()
    
    if t in substring:
        return True
        
    else:
        return False
