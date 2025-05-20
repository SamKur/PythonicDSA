# from itertools import combinations
def generate(numRows):
    """
    Function to generate the first numRows of Pascal's triangle.
    :param numRows: int -> Number of rows of Pascal's triangle to generate
    :return: List[List[int]] -> The first numRows of Pascal's triangle
    :example: Input: numRows = 5
        Output: [
          [1],
          [1, 1],
          [1, 2, 1],
          [1, 3, 3, 1],
          [1, 4, 6, 4, 1]
        ]
    :info: can be calculated using nCr formula = n! / r!(n-r)!
        OR, always starts with 1 and rest current element = previous row's current + prev
    """
    # TODO: Implement this function
    if numRows == 0:
        return []

    triangle = [[1]]

    for i in range(1, numRows):
        prev_row = triangle[-1]
        current_row = [1]

        for j in range(1, i):
            current_row.append(prev_row[j - 1] + prev_row[j])

        current_row.append(1)
        triangle.append(current_row)

    return triangle


print(generate(5))
