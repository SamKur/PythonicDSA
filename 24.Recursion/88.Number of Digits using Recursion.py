def count_digits(n):
    """
    Function to find the number of digits in a number using recursion.
    
    Parameters:
    n (int): The positive integer whose digits are to be counted.
    
    Returns:
    int: The number of digits in the integer.
    """
    # Your code here
    # Not trying pythonic way len(n) or [:-1] OFC LOL!
    
    if n==0: return 0
    return 1+count_digits(n//10) # (+) after the recursive call, it's not a tail call, and thus Python's call stack will grow.
    # By default python does not optimize TAIL CALL RECURSION
    
    # BEST way is iterative way, same time complexity O(log n) but space complexity from O(log n) to O(1)
    # if n == 0: return 1
    # count = 0
    # temp_n = abs(n)
    # while temp_n > 0:
    #     temp_n //= 10
    #     count += 1
    # return count


print(count_digits(12321))  # Output: 5