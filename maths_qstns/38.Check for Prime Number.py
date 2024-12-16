def is_prime(n):
    """
    Function to check if a number is prime.
    
    Parameters:
    n (int): The number to check.
    
    Returns:
    bool: True if n is prime, False otherwise.
    """
    # Your code here
    # Choosing the Right Method:
    # For small numbers: The optimized brute force method is often sufficient. 
    # - Iterate from 2 to the square root of the number, but skip even numbers (except 2).
    # For a range of numbers: The Sieve of Eratosthenes is efficient.
    # - Create a list of numbers from 2 to the desired limit.
    # - Mark the first unmarked number as prime.
    # - Mark all multiples of this prime number as not prime.
    # - Repeat the process with the next unmarked number.
    # For very large numbers: Miller-Rabin primality test 

    if n < 2 : return False
    if n == 2 : return True
    if n%3 == 0: return False
    for i in range(4, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

print(is_prime(125))