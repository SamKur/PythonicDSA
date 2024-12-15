def generate_right_angled_triangle(n):
    """
    Function to return a right-angled triangle of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The height of the triangle.
    
    Returns:
    list: A list of strings where each string represents a row of the triangle.

    Example:
    Input: 4
    Output: ['   *', '  **', ' ***', '****']
    """
    # Your code here
    li = list()
    for i in range(1,n+1):
        # print(('*'*i).rjust(width=n,fillchar=' ')) # str.rjust() takes no keyword arguments
        li.append(('*'*i).rjust(n,' '))
    return li


n = 4
print(generate_right_angled_triangle(n))