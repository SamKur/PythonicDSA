def is_palindrome(lst):
    """
    Function to check if a list is a palindrome.
    :param lst: List[int] -> List of integers
    :return: bool -> True if the list is a palindrome, False otherwise
    """
    # Using -ve index (Pythonic Way)
    # for i in range(0,len(lst)//2):
    #     if lst[i] != lst[-(i + 1)]: 
    #         return False
    # return True

    # Alt Way - universal using two pointers
    left = 0
    right = len(lst) - 1
    while left<right:
        if lst[left]!=lst[right]:
            return False
        left += 1
        right -= 1
    return True
    
print(is_palindrome([1, 2, 3, 2, 1]))