def generate_hollow_right_angled_triangle(n):
    """
    Function to return a hollow right-angled triangle of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The height of the triangle.
    
    Returns:
    list: A list of strings where each string represents a row of the triangle.
    """
    # Your code here
    hollow = []
    
    for i in range(n):
        if i==0:
            hollow.append('*')
            
        elif i == (n-1):
            hollow.append('*' * (n))
            
        else:
            spaces = ' ' * (i-1)
            stars = '*'
            hollow.append(stars + spaces + stars)
            
    return hollow
