def is_palindromic_tuple(tup):
    # Your code goes here
    # return tuple(tup[::-1])==tup  # pythonic way
    # instead of whole iteration we can use early detection
    # start and end position
    start = 0
    end = len(tup) - 1  
    
    while start < end:
        if tup[start] != tup[end]:
            return False
        start += 1
        end -= 1
    return True

t = ('a', 'b', 'c', 'b', 'a')
print(is_palindromic_tuple(t))