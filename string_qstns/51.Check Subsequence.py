def is_subsequence(s, t):
    """
    Function to check if t is a subsequence of s.
    
    Parameters:
    s (str): The original string.
    t (str): The target subsequence string.
    
    Returns:
    bool: True if t is a subsequence of s, False otherwise.

    Example:
    Input: s = "abcde", t = "ace"
    Output: True
    """
    index = 0
    for char in t:
        # string.find(value, start, end) -> returns index of the first occurrence, if not found returns -1
        index = s.find(char, index) + 1
        if index == 0:
            return False
    return True


print(is_subsequence("abcde", "ace"))