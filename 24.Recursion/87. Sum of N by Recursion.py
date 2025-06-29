import sys
sys.setrecursionlimit(5000) # Optionally we can tune the recursion limit

def sum_of_natural_numbers(n):
    """
    Function to calculate the sum of the first n natural numbers using recursion.
    
    Parameters:
    n (int): The non-negative integer for which the sum is to be calculated.
    
    Returns:
    int: The sum of the first n natural numbers.
    """
    # Your code here
    if n==0: return 0
    return n+sum_of_natural_numbers(n-1)

print(sum_of_natural_numbers(5))  # Output: 15
print(sum_of_natural_numbers(0))  # Output: 0