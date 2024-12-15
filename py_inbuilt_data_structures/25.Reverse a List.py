def reverse_list(lst):
    # Your code goes here
    # rev = []
    # for i in range(len(lst)-1,-1,-1):
    #     rev.append(lst[i])
    # return rev

    # OR simply
    # return lst[::-1]

    # OR without using any other list
    start = 0
    end = len(lst) - 1  # 5    
    # Swap elements until the two pointers meet in the middle
    while start < end:  # for odd length it will be equal hence no swap
        # Swap the elements at the start and end pointers
        lst[start], lst[end] = lst[end], lst[start]
        # Move the pointers towards the middle
        start += 1
        end -= 1
    return lst

print(reverse_list([12,2,344,3,11]))