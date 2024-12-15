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
    li = []
    for i in range(1,2*n):
        i = i if i<=n else 2*n-i
        spaces = abs(n-i)
        stars = 2*i-1
        st = ' '*spaces + '*'*stars + ' '*spaces
        li.append(st)
    return li

n = 2
print(generate_diamond(n))