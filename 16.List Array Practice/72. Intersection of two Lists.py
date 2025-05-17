def intersection(nums1, nums2):
    """
    Function to find the intersection of two integer arrays.
    :param nums1: List[int] -> First array of integers
    :param nums2: List[int] -> Second array of integers
    :return: List[int] -> An array of unique integers present in both arrays
    """
    # TODO: Implement this function
    # common = []
    # for num in nums1:
    #     if num in nums2 and num not in common: # O(log n*m) complexity
    #         common.append(num)
    # return common
    set1 = set(nums1)
    intersection_set = set()
    for num in nums2:
        if num in set1: # The O(1) average-case complexity for set lookups - total complexity - O(n + m)
            intersection_set.add(num)
    return list(intersection_set)


print(intersection(nums1 = [4, 9, 5], nums2 = [9, 4, 9, 8, 4]))