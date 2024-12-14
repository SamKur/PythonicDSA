def generate_diamond(n):
    """
    Function to return a diamond pattern of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The number of rows for the upper part of the diamond.
    
    Returns:
    list: A list of strings where each string represents a row of the diamond.

    Example:
    Input: 3
    Output: ['  *  ', ' *** ', '*****', ' *** ', '  *  ']
    """
    # Your code here
    op = []
    for i in range(1, 2 * n):
        op.append(  ' ' * abs(n - i) + '*' * (2 * (n - abs(n - i)) - 1) + ' ' * abs(n - i)  )
        # op.append(' '*abs(n-i) + '*'*(n-abs(n-i)) + ' '*abs(n-i))
    return op

print(generate_diamond(3))