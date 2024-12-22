def is_substring(s, t):
    """
    Function to check if string t is a substring of string s without using built-in functions and recursion.
    
    Parameters:
    s (str): The main string.
    t (str): The string to check as a substring.
    
    Returns:
    bool: True if t is a substring of s, False otherwise.
    """
    # Your code here
    for i in range(len(s) - len(t) + 1):  # Loop through all possible starting positions in `s`
        match = True
        for j in range(len(t)):  # Check each character in `t`
            if s[i + j] != t[j]:  # If there's a mismatch, break
                match = False
                break
        if match:  # If all characters of `t` match
            return True
    return False  # If no match is found

print(is_substring("zabcde", "abe")) # False
