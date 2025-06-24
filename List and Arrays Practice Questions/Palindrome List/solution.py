def is_palindrome(lst):
    """
    Function to check if a list is a palindrome.
    :param lst: List[int] -> List of integers
    :return: bool -> True if the list is a palindrome, False otherwise
    """
    # TODO: Implement this function
    start = 0
    end = len(lst) - 1
    
    while start <= end:
        if lst[start] != lst[end]:
            return False
        start += 1
        end -= 1
            
    return True
    pass
