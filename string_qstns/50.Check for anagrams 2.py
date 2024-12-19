def is_anagram(s, t):
    """
    Function to check if t is an anagram of s.
    
    Parameters:
    s (str): The first input string.
    t (str): The second input string.
    
    Returns:
    bool: True if t is an anagram of s, False otherwise.
    """
    # Your code here
    # In udemy code the previous one was failing
    if len(s) != len(t):
        return False
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    for char in t:
        # char_count[char] = char_count.get(char) - 1
        if char not in char_count or char_count[char] == 0:
            return False  # Early exit if character is missing or count is zero
        char_count[char] -= 1
    return sum(char_count.values())==0
    # return all(value == 0 for value in char_count.values())


print(is_anagram('', ''))