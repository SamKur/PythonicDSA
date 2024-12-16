def merge_three_dictionaries(dict1, dict2, dict3):
    """
    Input: ({'x': 10, 'y': 20}, {'z': 30}, {'a': 40, 'b': 50})
    Output: {'x': 10, 'y': 20, 'z': 30, 'a': 40, 'b': 50}
    """
    # Your code goes here
    d = dict1.copy()
    for k,v in dict2.items():
        d[k]=v
    for k,v in dict3.items():
        d[k]=v
    return d
    

d1, d2, d3 = ({'x': 10, 'y': 20}, {'z': 30}, {'a': 40, 'b': 50})
print(merge_three_dictionaries(d1,d2,d3))
