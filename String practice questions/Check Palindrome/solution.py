def is_palindrome(s):
    """
    Function to check if the input string is a palindrome.
    
    Parameters:
    s (str): The input string to check.
    
    Returns:
    bool: True if the string is a palindrome, False otherwise.
    """
    # Your code here
    new_s = ''.join(char.lower() for char in s if char.isalnum())
    start = 0
    end = len(new_s) - 1
    
    while start < end:
        if new_s[start] != new_s[end]:
            return False
        start += 1
        end -= 1
        
    return True
