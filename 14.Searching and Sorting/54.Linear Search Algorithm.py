def linear_search(arr, target):
    # return the index of the first occurrence
    i = 0
    while i < len(arr):
        if arr[i] == target:
            return i
        i+=1
    return -1 
print(linear_search([3, 7, 2, 5], 2)) # 2