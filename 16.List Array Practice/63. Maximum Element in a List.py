def find_max_element(lst):
    """
    Function to find the maximum element in a list.
    :param lst: List[int] -> List of integers
    :return: int -> The maximum element in the list
    """
    # TODO: Implement this function
    # return max(lst)
    maxx = lst[0]
    for item in lst:
        if item>maxx:
            maxx=item
    return maxx

print(find_max_element([2342,323,2342,1,-3231]))