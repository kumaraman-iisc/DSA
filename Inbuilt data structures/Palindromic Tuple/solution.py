def is_palindromic_tuple(tup):
    # Your code goes here
    start = 0
    end = len(tup) - 1
    while start < end:
        if tup[start] != tup[end]:
            return False
        start += 1
        end -= 1
    return True
