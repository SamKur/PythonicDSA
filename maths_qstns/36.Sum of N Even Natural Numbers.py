def sum_of_even_numbers(n):
    """
    Function to return the sum of the first n even natural numbers.
    
    Parameters:
    n (int): The number of even numbers to sum.
    
    Returns:
    int: The sum of the first n even natural numbers.
    """
    # Your code here
    # 1. By iterative way OR list comprehension ->
    # return sum([2 * i for i in range(1, n + 1)])
    # 2. By maths formula - n(n+1) for EVENs || n^2 for ODDs

    sum = 0
    # for i in range(1,2*n+1):
        # if i%2==0: sum += i   #OR
    # for i in range(2,2*n+1,2): #OR
    #     sum += i
    current_even_num = 2
    for i in range(n):
        sum = sum + current_even_num
        current_even_num = current_even_num + 2  
    return sum

print(sum_of_even_numbers(10))