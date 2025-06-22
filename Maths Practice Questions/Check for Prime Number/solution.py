def is_prime(n):
    """
    Function to check if a number is prime.
    
    Parameters:
    n (int): The number to check.
    
    Returns:
    bool: True if n is prime, False otherwise.
    """
    # Your code here
    factors = 0
    
    for i in range(1, n+1):
        if n % i == 0:
            factors += 1
            
    if factors == 2:
        return True
        
    else:
        return False
