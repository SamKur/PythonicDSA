def binary_to_decimal(binary_str):
    """
    Function to convert a binary string to its decimal integer representation.
    
    Parameters:
    binary_str (str): The binary string to convert.
    
    Returns:
    int: The decimal representation of the binary string.
    """
    # Your code here
    return int(binary_str, base = 2)  # Base can be 8 for octal->decimal , 16 for hexadecimal->decimal

