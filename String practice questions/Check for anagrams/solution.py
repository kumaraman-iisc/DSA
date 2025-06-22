def is_anagram(s, t):
    """
    Function to check if t is an anagram of s.
    
    Parameters:
    s (str): The first input string.
    t (str): The second input string.
    
    Returns:
    bool: True if t is an anagram of s, False otherwise.
    """
    # Your code here
    if len(s) != len(t):
        return False
        
    count_s = [0] * 26
    count_t = [0] * 26
    
    s = s.lower()
    t = t.lower()
    
    for char in s:
        count_s[ord(char) - ord('a')] += 1
        
    for char in t:
        count_t[ord(char) - ord('a')] += 1
        
    for i in range(26):
        if count_s[i] != count_t[i]:
            return False
            
    return True
        
    
