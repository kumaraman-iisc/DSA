def searchRange(nums, target):
    """
    Function to find the starting and ending position of a given target value in a sorted array.
    If the target is not found, return [-1, -1].
    """
    def find_first(nums, target):
        left, right = 0, len(nums) - 1
        first = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                first = mid
                right = mid - 1
        return first

    def find_last(nums, target):
        left, right = 0, len(nums) - 1
        last = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                last = mid
                left = mid + 1
        return last

    first = find_first(nums, target)
    last = find_last(nums, target)
    return [first, last]
