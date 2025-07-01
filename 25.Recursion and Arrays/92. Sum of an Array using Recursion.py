def recursive_sum(arr, acc=0):
    """
    Function to calculate the sum of an array using recursion.
    
    Parameters:
    arr (list of int): The array of integers.
    
    Returns:
    int: The sum of the array elements.
    """
    # Your code here
    if len(arr) == 0: return acc # base case
    
    # head recursion
    # return arr[0] + recursive_sum(arr[1:]) # O(n) and O(n^2)
    
    # tail recursion
    acc += arr[0]
    return recursive_sum(arr[1:], acc)

print(recursive_sum([1,2,5,2]))