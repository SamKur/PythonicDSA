def move_zeroes(nums):
    """
    Function to move all 0's to the end of the array while maintaining the order of non-zero elements.
    :param nums: List[int] -> A list of integers
    :return: None -> The list is modified in place
    """
    pos = 0
    for i in range(len(nums)):
        if nums[i]!=0:
            nums[i], nums[pos] = nums[pos], nums[i]
            pos += 1
    print(nums)

print(move_zeroes([4, 2, 4, 0, 0, 3, 0, 5, 1, 0]))