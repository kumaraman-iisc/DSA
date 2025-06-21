def count_even_odd(lst):
    # Your code goes here
    count_even = 0
    count_odd = 0
    
    for num in lst:
        if num%2 == 0:
            count_even += 1
            
        else:
            count_odd += 1
            
    return (count_even, count_odd)
    pass
