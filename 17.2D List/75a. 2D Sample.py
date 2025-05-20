def generate(numRows):
    """
    Function to generate Simple 2D list with given number of rows.
    :example: Input: numRows = 5
        Output: [
          [1],
          [1, 2],
          [1, 2, 3],
          [1, 2, 3, 4],
          [1, 2, 3, 4, 5]
        ]
    """
    # TODO: Implement this function
    pass
    li2d = []
    for i in range(1, numRows + 1):
        li = []
        for j in range(1, i+1):
            li.append(j)
        li2d.append(li)
    return li2d


print(generate(5))
