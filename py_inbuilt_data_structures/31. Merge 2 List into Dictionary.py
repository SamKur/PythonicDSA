def merge_lists_to_dictionary(keys, values):
    """
    Example:
    Input: keys = ['x', 'y', 'z'], values = [10, 20, 30]
    Output: {'x': 10, 'y': 20, 'z': 30}
    """
    # Your code goes here
    if len(keys) != len(values):
        return "Error! Size mismatch"
    di = dict() # or {}
    # for k,v in zip(keys,values):
    #     di[k]=v
    # return di
    for i in range(len(keys)):
        di[keys[i]]=values[i]
    return di

keys = ['x', 'y', 'z']
values = [10, 20, 30]
print(merge_lists_to_dictionary(keys, values))