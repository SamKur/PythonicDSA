def fibonacci(n):
    """
    Function to calculate the nth Fibonacci number using recursion.
    
    Parameters:
    n (int): The non-negative integer for which the Fibonacci number is to be calculated.
    
    Returns:
    int: The nth Fibonacci number.
    """
    # Your code here
    # 0, 1, then addition of last 2
    if n==0: return 0
    if n==1: return 1
    else: return fibonacci(n-1) + fibonacci(n-2)
    # Time Complexity: O(2^n) - Exponential time complexity due to the recursive calls.
    # Space Complexity: O(n) - The maximum depth of the recursion stack is n.

    # Better Approach - Itrative O(n) & O(1)

print(fibonacci(12))