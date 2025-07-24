def find_max_consecutive_ones(nums):
    """
    Function to find the maximum number of consecutive 1's in a binary array.
    :param nums: List[int] -> A binary array where each element is either 0 or 1
    :return: int -> The maximum number of consecutive 1's
    """
    # TODO: Implement this function
    # pythonic implementation - using ordered_dict maybe!?
    # from itertools import groupby
    # def find_max_consecutive_ones(nums):
    #     return max((sum(g) for k, g in groupby(nums) if k == 1), default=0)

    # counts = [0]
    # for num in nums:
    #     if num == 1:
    #         counts[-1] += 1
    #     else:
    #         counts.append(0) # time O(n) & space O(n)
    # return max(counts)

    # more optimized - time O(n) & space O(1)
    max_count = current_count = 0
    for num in nums:
        if num == 1:
            current_count += 1
            max_count = max(max_count, current_count)
        else:
            current_count = 0
    return max_count

print(find_max_consecutive_ones(nums = [1, 0, 1, 1, 0, 1, 1, 1, 1]))
print(find_max_consecutive_ones(nums = [1, 1, 1]))
print(find_max_consecutive_ones(nums = [0, 0, 0]))
