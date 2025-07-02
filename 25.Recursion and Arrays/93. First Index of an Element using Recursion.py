def find_first_index(arr, element):
    """
    Function to find the first index of a given element in an array using recursion.
    
    Parameters:
    arr (list of int): The array to search through.
    element (int): The element to find.
    
    Returns:
    int: The first index of the element in the array, or -1 if not found.
    """
    # Your code here
    # Head Recursive - Complexity O(n^2) and O(n^2)  
    if not arr: return -1
    if arr[0] == element: return 0
    recursive_result = find_first_index(arr[1:], element)
    if recursive_result == -1: return -1
    return recursive_result+1
    


print( find_first_index([1, 2, 3, 2, 4, 2], 2) )