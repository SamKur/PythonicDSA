def is_subsequence(s, t):
    """
    Function to check if t is a subsequence of s without using built-in functions.
    
    Parameters:
    s (str): The original string.
    t (str): The target subsequence string.
    
    Returns:
    bool: True if t is a subsequence of s, False otherwise.
    """
    i, j = 0, 0
    
    while i < len(s) and j < len(t):
        if s[i] == t[j]:    # If the characters match, move the pointer for t
            j += 1
        i += 1  # Always move the pointer for s
    
    return j == len(t)

print(is_subsequence("abcde", "ace"))