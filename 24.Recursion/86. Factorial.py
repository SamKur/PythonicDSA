def factorial(n):
    """
    Function to calculate the factorial of a non-negative integer n using recursion.

    Parameters:
    n (int): The non-negative integer for which the factorial is to be calculated.

    Returns:
    int: The factorial of n.
    """
    # Your code here
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


print(factorial(5))
