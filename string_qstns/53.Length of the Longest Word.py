def longest_word_length(s):
    """
    Function to find the length of the longest word in a string without using built-in functions.
    
    Parameters:
    s (str): The input string.
    
    Returns:
    int: The length of the longest word.
    
    Example:
    Input: s = "The quick brown fox jumps over the lazy dog"
    Output: 5
    """
    # Your code here
    max_count = 0
    count = 0
    for char in s:
        if char != ' ':
            count = count + 1
            if count>max_count:
                max_count = count
        else: count = 0
    return max_count


print(longest_word_length("The quick brown fox jumps over the lazy dog"))