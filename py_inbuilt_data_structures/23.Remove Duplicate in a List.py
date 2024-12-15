def remove_duplicates(lst):
    # Your code goes here
    # preserve the order, else we can use list(set(lst))
    uniques = []
    for item in lst:
        if item not in uniques:
            uniques.append(item)
    return uniques

l = [1, 2, 2, 4, 3, 7, 4, 4, 5]
print(remove_duplicates(lst=l))