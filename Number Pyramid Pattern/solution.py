def generate_number_pyramid(n):
    """
    Function to return a pyramid pattern of numbers of height n as a list of strings.
    
    Parameters:
    n (int): The height of the pyramid.
    
    Returns:
    list: A list of strings where each string represents a row of the pyramid pattern.
    """
    # Your code here
    numbers = []
    #num = 1
    
    for i in range(1, n+1):
        spaces = ' ' * (n - i)
        num = ' '.join(str(x) for x in range(1,i+1))
        numbers.append(spaces + num + spaces)
        
    return numbers
