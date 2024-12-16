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

    # Simplest way
    # if n < 2:
    #     return False  # Numbers less than 2 are not prime
    # for i in range(2, int(n**0.5) + 1):  # Check divisors from 2 to whole √n
    #     if n % i == 0:
    #         return False
    # return True

    # optimizing the code
    # if n < 2 : return False  # this code will fail in case of 25 49 etc for odd composite numbers.
    # if n == 2 : return True
    # if n%2 ==0 or n%3 == 0: return False
    # for i in range(4, int(n**0.5) + 1, 2):
    #     if n % i == 0:
    #         return False
    # return True

    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False  # Eliminate multiples of 2 and 3
    
    # Check divisors of the form 6k ± 1 (all primes are here - 5 , 7, 11, 17)
    for i in range(5, int(n**0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    # or use while instead of for and int function
    # i = 5
    # while i * i <= num:
    #     if num % i == 0 or num % (i + 2) == 0:
    #         return False
    #     i += 6
    return True

print(is_prime(125))