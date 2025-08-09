def is_perfect_square(num):
    """
    Function to check if a number is a perfect square without using built-in functions.
    
    Parameters:
    num (int): The number to check.
    
    Returns:
    bool: True if num is a perfect square, False if num is not.
    """
    # return int(num**(.5))==num**(.5) # pythonic way
    if num < 1:
        return False  # No perfect squares for numbers less than 1
    i = 1
    while i * i <= num:
        if i * i == num:
            return True  # Found a perfect square
        i += 1
    return False

print(  is_perfect_square(37)   )