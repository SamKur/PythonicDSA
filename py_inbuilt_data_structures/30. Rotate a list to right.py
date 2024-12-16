def rotate_list(lst, k):
    # Your code goes here
    length = len(lst)
    if k == length or k == 0 or length == 0:
        return lst
    if k > length:  # to optimize repeats
        k = k % length
    li = []
    for i in range(length-k , length): # if k=3 -> r(2,5)
        li.append(lst[i])
    for i in range(length-k): # r(2)
        li.append(lst[i])
    return li


print(rotate_list(lst = [10, 20, 30, 40, 50], k = 3))