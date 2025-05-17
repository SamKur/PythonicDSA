def find_missing_number(nums):
    """
    Function to find the missing number in the array.
    :param nums: List[int] -> A list of distinct integers in the range [0, n]
    :return: int -> The missing number in the range
    """
    size = len(nums)
    for i in range(size):
        if i not in nums:
            return i
    return size

    # OR by formula
    # n = len(nums)
    # total = (n * (n + 1)) // 2
    # return total - sum(nums)

print(find_missing_number([0, 1]))
print(find_missing_number([8, 7, 6, 4, 3, 2, 0, 1]))