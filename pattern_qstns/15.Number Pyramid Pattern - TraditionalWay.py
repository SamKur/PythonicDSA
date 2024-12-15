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
    pyramid = []
    for i in range(1, n+1):
        row = ""
        row += ' '*(n-i) # starting spaces
        
        for j in range(1, i+1):  
            row += str(j) + " "
            # row += str(j) + " " if j<i else row += str(j)  #OR,
        row = row[:-1]   # striping last extra space

        row += ' '*(n-i) # ending spaces
        # print(len(row))
        pyramid.append(row)
    return pyramid

if __name__=="__main__":
    num = 2
    print(generate_number_pyramid(num), sep='\n')