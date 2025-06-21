def find_largest(numbers):
    # Your code goes here
    largest_num = numbers[0]
    
    for num in numbers:
        if not numbers:
            raise ValueError("List is empty")
            
        if num > largest_num:
            largest_num = num
    return largest_num
    pass
