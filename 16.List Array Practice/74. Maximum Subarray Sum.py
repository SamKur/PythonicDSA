def max_subarray_sum(arr):
    """
    Given an array of integers, find the maximum sum of any subarray.

    Parameters:
    arr (List[int]): List of integers.

    Returns:
    int: Maximum sum of any subarray.
    """
    # Implement the function

    # AKA Kadane's Algorithm -  O(n) time and O(1) space
    max_current = max_global = arr[0]
    for num in arr[1:]:
        max_current = max(num, max_current + num)
        max_global = max(max_global, max_current)
    return max_global


print(max_subarray_sum(arr=[-2, 1, -3, 4, -1, 2, 1, -5, 4]))
