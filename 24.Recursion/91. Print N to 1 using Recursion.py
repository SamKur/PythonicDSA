def count_down(n, li=None):
    """
    Function to return a list of integers from n to 1 using recursion.
    
    Parameters:
    n (int): The positive integer representing the starting point of the range.
    
    Returns:
    list: A list of integers from n to 1.
    """
    # Your code here
    # Tail Recursion
    # if n==0: return li
    # if li == None: li = []
    # li.append(n)
    # return count_down(n-1, li)

    # Head Recursion
    if n==0: return []
    return [n]+count_down(n-1)

print(count_down(5))