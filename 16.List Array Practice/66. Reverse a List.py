def reverse_list(lst):
    """
    Function to reverse the order of elements in a list.
    :param lst: List[int] -> List of integers
    :return: List[int] -> The list with elements in reversed order
    """
    left = 0
    right = len(lst)-1

    while left<right:
        # in python we can also easily swap using
        # lst[left], lst[right] = lst[right], lst[left]
        val = lst[left]
        lst[left] = lst[right]
        lst[right] = val
        left += 1
        right -= 1
    return lst

print(reverse_list( [5, 4, 3, 2, 1] ))
