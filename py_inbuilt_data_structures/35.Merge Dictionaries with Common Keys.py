def merge_dicts_with_overlapping_keys(dicts):
    """
    Example:
    Input: [{'a': 1, 'b': 2}, {'b': 3, 'c': 4}, {'c': 5, 'd': 6}]
    Output: {'a': 1, 'b': 5, 'c': 9, 'd': 6}
    """
    # Your code goes here
    # To get each item, I can iterate through or use unpacking operator *dict
    final = {}  # OR i can store entire copy first dictionary
    for d in dicts: # then iterate from 2nd 
        for k, v in d.items():
            if k in final:
                final[k] += v
            else:
                final[k] = v
    return final
    


dicts = [{'a': 1, 'b': 2}, {'b': 3, 'c': 4}, {'c': 5, 'd': 6}]
print(merge_dicts_with_overlapping_keys(dicts))