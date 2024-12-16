def int_to_binary(n):
    """
    Function to convert an integer to its binary representation.
    
    Parameters:
    n (int): The integer to convert.
    
    Returns:
    str: The binary representation of the integer.
    """
    # Your code here
    b = bin(n) # pythonic way
    if b[0]=='-':
        return '-'+b[3:]
    return b[2:]


print(int_to_binary(-5))