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
    if n <= 0:
        return []

    diamond = []

    for i in range(1, 2 * n):
        if i <= n:  # Upper & middle row
            row_index = i
        else:  # Lower
            row_index = 2 * n - i

        spaces = ' ' * (n - row_index)
        stars = '*' * (2 * row_index - 1)
        diamond.append(spaces + stars + spaces)

    return diamond

if __name__ == "__main__":
    n = 3
    result = generate_diamond(n)
    for row in result:
        print(row)
