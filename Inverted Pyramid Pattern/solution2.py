
def generate_inverted_pyramid(n):
    """
    Function to return an inverted pyramid pattern of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The number of rows in the inverted pyramid.
    
    Returns:
    list: A list of strings where each string represents a row of the inverted pyramid.
    """
    # Initialize an empty list to store the rows of the pyramid
    pyramid = []
    
    # Loop through each row from 1 to n
    for i in range(1, n + 1):
        # Number of stars in the current row is 2 * (n - i + 1) - 1
        stars = '*' * (2 * (n - i + 1) - 1)
        # Number of leading spaces to center the stars is i - 1
        spaces = ' ' * (i - 1)
        # Add the centered row to the list
        pyramid.append(spaces + stars + spaces)
    
    # Return the list of pyramid rows
    return pyramid
