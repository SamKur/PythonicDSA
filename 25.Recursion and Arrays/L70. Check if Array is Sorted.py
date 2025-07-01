def check_if_sorted(arr):
    if len(arr) in (0,1): return True # 1. Base Case - FIXED

    # tail recursion - 2nd approach
    # if arr[0] > arr[1]: return False
    # return check_if_sorted(arr[1:])   # Complexity O(N^2) and O(N^2)

    # head recursion - 3rd approach
    ans = check_if_sorted(arr[1:])
    if (arr[0] > arr[1]) or (ans==False) : return False # current node chk
    return True

    # Naive iterative solution - EASIEST - Complexity O(n) and O(1)
    # for i in range(len(arr)-1):
    #     if arr[i]>arr[i+1]:
    #         return False
    # return True


print(check_if_sorted([12,34,35,70,81,13,90]))