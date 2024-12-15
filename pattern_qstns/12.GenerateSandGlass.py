def generate_sandglass(n):
    """
    Function to return a sandglass pattern of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The height of the sandglass (Upto middle portion).
    
    Returns:
    list: A list of strings where each string represents a row of the sandglass pattern.

    Example:
    Input: 3
    Output: ['*****', ' *** ', '  *  ', ' *** ', '*****']
    """
    # Your code here
    pattern = []
    
    # Top half (inverted triangle, including middle line *)
    for i in range(n):
        spaces = ' ' * i
        stars = '*' * (2 * (n - i) - 1)
        pattern.append(spaces + stars + spaces)
    
    # Bottom half (normal triangle)
    for i in range(1, n):  # Start from 1 to skip the middle row
        spaces = ' ' * (n - i - 1)
        stars = '*' * (2 * i + 1)
        pattern.append(spaces + stars + spaces)
    
    return pattern


num = 3
print(generate_sandglass(num))