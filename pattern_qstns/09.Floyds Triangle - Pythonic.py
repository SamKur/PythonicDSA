def generate_floyds_triangle(n):
    """
    Function to return the first n rows of Floyd's Triangle as a list of strings.
    
    Parameters:
    n (int): The number of rows in the triangle.
    
    Returns:
    list: A list of strings where each string represents a row of Floyd's Triangle.
    """
    # Initialize an empty list to store the rows of the triangle
    triangle = []
    
    # Initialize the first number to be used in the triangle
    start = 1
    
    # Loop through each row from 1 to n
    for i in range(1, n + 1):
        # Create a row by collecting the next i numbers
        row = ' '.join(str(start + j) for j in range(i))
        # Append the row to the list
        triangle.append(row)
        # Update the current number for the next row
        start += i
    
    # Return the list of rows
    return triangle

print(generate_floyds_triangle(4))