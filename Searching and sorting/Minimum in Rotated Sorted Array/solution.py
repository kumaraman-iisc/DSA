def findMin(nums):
    # Implement your solution here
    size = len(nums)
    smallest = nums[0]
    
    for index in range(0, size):
        if smallest > nums[index]:
            smallest = nums[index]
            
    return smallest
    pass
