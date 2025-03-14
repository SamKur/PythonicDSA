def rotate_left(ARR, D):
    """
    Function to rotate the list to the left by D positions.
    :param ARR: List[int] -> The list of integers
    :param D: int -> The number of positions to rotate
    :return: List[int] -> The list after rotation
    """
    # Pythonic way
    # left = 0
    # while left<D:
        # ARR.append(ARR.pop(0))
        # left += 1
    # return ARR

    # OR
    # D = D % len(ARR)  # Handle cases where D is larger than the size of the list
    # return ARR[D:] + ARR[:D]
    
    # OR generic way
    lenn = len(ARR)
    D = D % lenn # Handle cases where D is larger than the size of the list
    
    def reverse(arr, start, end):
        while start<end:
            val = arr[start]
            arr[start]=arr[end]
            arr[end]=val
            start += 1
            end -= 1
    
    # step1 : reverse first D element
    reverse(ARR, 0, D-1)
    # step2 : reverse elements after D
    reverse(ARR, D, lenn-1)
    # step3 : reverse the entire list
    reverse(ARR, 0, lenn-1)

    return ARR

print(rotate_left( ARR = [1, 2, 3, 4, 5], D = 2 )) # [3, 4, 5, 1, 2]