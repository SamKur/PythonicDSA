def is_subset(lst1, lst2):
    """
    checking if lst1 is subset of lst2
    ie all items of lst1 must be present in lst2 
    """
    # Your code goes here
    # Brute Force method, without using membership check
    for i in lst1:
        found = False
        for j in lst2:
            if i == j:  # 5 == 1 goest to next itr # 5 == 2
                found = True
                break
        if found == False:
            return False
    return True




lst1 = [5, 2, 3]
lst2 = [1, 2, 3, 4, 5]
print(is_subset(lst1,lst2))