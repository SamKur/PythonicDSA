def count_to_n(n, li = None):
    """
    Function to return a list of integers from 1 to n using recursion.
    
    Parameters:
    n (int): The positive integer representing the upper limit of the range.
    
    Returns:
    list: A list of integers from 1 to n.
    """
    # Your code here # This is Tail Recursion
    # if li==None: li =[]
    # if n==0: li.reverse(); return li
    # li.append(n)
    # return count_to_n(n-1, li)
    
    # HEAD recursion
    if n==0: return []
    li2 = count_to_n(n-1)
    li2.append(n)
    return li2
    
print(count_to_n(5))  # Output: [1, 2, 3, 4, 5]

# Time Complexity: O(n) - Linear time complexity as we are making n recursive calls.
# Space Complexity: O(n) - The maximum depth of the recursion stack is n, and we are also storing the result in a list of size n.
# Note: The space complexity can be reduced to O(1) if we use an iterative