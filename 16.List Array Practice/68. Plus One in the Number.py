def plus_one(digits):
    """
    Function to increment a large integer represented as a list of digits by one.
    :param digits: List[int] -> List of digits representing the large integer
    :return: List[int] -> The list representing the integer after incrementing
    """
    # Below is inefficient, may lead to errors like - IntegerOverflow
    # st = ''
    # li = []
    # for n in digits:
    #     st += str(n)
    # st_num = int(st)
    # op_num = st_num + 1
    # op_str = str(op_num)
    # for each in op_str:
    #     li.append(each)
    # return li

    # Efficient Approach (Generic) - modify the list directly using carry propagation
    n = len(digits)

    for i in range(n-1, -1, -1): # Start from the last digit
        if digits[i] < 9:        
            digits[i] += 1
            return digits        # Return early if no carry needed
        digits[i] = 0            # if digit is 9, set it as 0 nd continue next iteration

    return [1]+digits            # If all digits were 9, we need an extra leading 1

print (plus_one(digits = [1, 0, 9, 9])) # [1, 1, 0, 0]
print (plus_one(digits = [1, 0, 3, 2])) # [1, 0, 3, 3]