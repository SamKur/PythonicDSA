def generate_hollow_right_angled_triangle(n):
    """
    Function to return a hollow right-angled triangle of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The height of the triangle.
    
    Returns:
    list: A list of strings where each string represents a row of the triangle.

    Exa,ple:
    Input: 5
    Output: ['*', '**', '* *', '*  *', '*****']
    """
    # Your code here
    li = []
    for i in range(1,n+1):
        if i in (1,2,n):
            li.append('*' * i)
        else:
            li.append('*' + ' '*(i-2) + '*')
    return li


if __name__=="__main__":
    num = 2
    print(*generate_hollow_right_angled_triangle(num), sep='\n')