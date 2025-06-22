def int_to_binary(n):
    """
    Function to convert an integer to its binary representation.
    
    Parameters:
    n (int): The integer to convert.
    
    Returns:
    str: The binary representation of the integer.
    """
    # Your code here
    if n == 0:
        return "0"
 
    binary_representation = ""
    
    is_negative = n < 0
    if is_negative:
        n = -n
 
    while n > 0:
        remainder = n % 2
        binary_representation = str(remainder) + binary_representation
        n = n // 2
 
    if is_negative:
        binary_representation = "-" + binary_representation
 
    return binary_representation
