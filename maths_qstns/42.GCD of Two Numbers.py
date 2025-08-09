def gcd(n, m):
    """
    Function to find the GCD of two integers without using built-in functions and recursion.
    
    Parameters:
    n (int): The first integer.
    m (int): The second integer.
    
    Returns:
    int: The GCD (gosagu) of n and m.
    """
    # Your code here
    # Complexity - O(n) and O(1)
    # start = min(n,m)
    # for i in range(start, 0, -1):
    #     if n%i==0 and m%i==0:
    #         return i

    # Better Approach - O(log n) and O(1)
    # Any number that divides both a and b will also divide a%b
    # Euclidean formula -> gcd(a, b) = gcd(b, a % b) 
    while m != 0:
        n, m = m, n % m
    return n

print(gcd(48,18))
print(gcd(18,49))