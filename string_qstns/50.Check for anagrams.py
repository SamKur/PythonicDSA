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
    if len(s) != len(t):
        return False
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    # print(char_count)
    # Now I can do the same for t then compare the dicts
    # OR 
    for char in t:
        char_count[char] = char_count.get(char) - 1
    # print(char_count)
    # Now will check if every value is zero
    # return sum(char_count.values())==0 # error in empty string
    return all(value == 0 for value in char_count.values())


print(is_anagram('', ''))