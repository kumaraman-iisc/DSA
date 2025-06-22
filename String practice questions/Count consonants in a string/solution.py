def count_consonants(s):
    """
    Function to count the number of consonants in the input string.
    
    Parameters:
    s (str): The input string to check for consonants.
    
    Returns:
    int: The count of consonants in the input string.
    """
    # Your code here
    vowels ='aeiouAEIOU'
    count = 0
    s = ''.join(char for char in s if char.isalnum())
    
    for char in s:
        if char not in vowels:
            count += 1
            
    return count
