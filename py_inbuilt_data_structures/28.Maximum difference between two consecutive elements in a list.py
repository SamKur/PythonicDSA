def max_consecutive_difference(lst):
    # Your code goes here
    # Use Brute Force Approach
    max_diff = 0
    for idx in range(len(lst)-1):
        diff = abs(lst[idx]-lst[idx+1])
        if diff > max_diff:
            max_diff = diff
    return max_diff
    # OR same thing by list comprehension
    # return max(abs(lst[i] - lst[i + 1]) for i in range(len(lst) - 1))
lst = [1, 7, 3, 10, 5, 9]
# lst = [2] # edge case automatically handled
print(max_consecutive_difference(lst))