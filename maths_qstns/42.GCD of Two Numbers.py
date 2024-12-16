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
    for i in range(n,0,-1):  # or, start with min(n,m)
        if n%i==0 and m%i==0:
            return i
        
print(gcd(48,18))