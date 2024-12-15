def merge_two_sorted_lists(list1, list2):
    # Your code goes here

    # li = []
    # for i in list1:
    #     for j in list2:
    #         if i>j:
    #             li.append(j)  
    #             list2.remove(j)  # this leads to unpredicatable behaviour
    #         else:
    #             li.append(i)
    #             list1.remove(i)
    # return li

    merged_list = []
    i, j = 0, 0 # starting indexes

    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1

    # Append remaining elements from the longer list
    merged_list.extend(list1[i:])
    merged_list.extend(list2[j:])

    return merged_list


list1, list2  = [1, 4, 7], [2, 3, 5, 8]
print(merge_two_sorted_lists(list1, list2))