def generate_floyds_triangle(n):
    """
    Function to return the first n rows of Floyd's Triangle as a list of strings.
    
    Parameters:
    n (int): The number of rows in the triangle.
    
    Returns:
    list: A list of strings where each string represents a row of Floyd's Triangle.
    if n=3 => o/p = ['1', '2 3', '4 5 6']
    """
    # Your code here
    li = []
    no = 0
    
    for i in range(1, n+1):
        st = ''
        for j in range(1, i+1):
            no = no + 1
            st = st + str(no) + ' '
        li.append(st.rstrip())
    return li


print(generate_floyds_triangle(5))  