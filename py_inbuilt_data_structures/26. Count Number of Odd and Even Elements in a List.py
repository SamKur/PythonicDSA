def count_even_odd(lst):
    # Your code goes here
    odds = 0
    evens = 0
    for i in lst:
        if i%2 == 0:
            evens += 1
        else:
            odds += 1
    return evens,odds

lst = [1, 2, 3, 4, 5]
print(count_even_odd(lst))