def sum_of_elements(lst):
    """
    Function to find the sum of all elements in the list.
    :param lst: List[int] -> List of integers
    :return: int -> The sum of all elements in the list
    """
    # TODO: Implement this function
    summ = 0
    for item in lst:
        summ = summ + item
    return summ


print(sum_of_elements([342,432423,54324,12,0,-500000]))