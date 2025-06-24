def find_max_element(lst):
    """
    Function to find the maximum element in a list.
    :param lst: List[int] -> List of integers
    :return: int -> The maximum element in the list
    """
    # TODO: Implement this function
    greatest = lst[0]
    
    for i in lst:
        if i > greatest:
            greatest = i
            
    return greatest
    pass
