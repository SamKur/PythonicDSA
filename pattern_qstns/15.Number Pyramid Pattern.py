def generate_number_pyramid(n):
    """
    Function to return a pyramid pattern of numbers of height n as a list of strings.
    
    Parameters:
    n (int): The height of the pyramid.
    
    Returns:
    list: A list of strings where each string represents a row of the pyramid pattern.

    Example:
    Input: 4
    Output: ['   1   ', '  1 2  ', ' 1 2 3 ', '1 2 3 4']
    """
    # Your code here
    li = []
    for i in range(1,n+1):
        st = ' '.join(str(j) for j in range(1,i+1))
        li.append(st.center(2*n-1))  #justify
    return li

if __name__=="__main__":
    num = 5
    print(*generate_number_pyramid(num), sep='\n')