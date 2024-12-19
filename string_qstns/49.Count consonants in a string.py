def count_consonants(s):
    """
    Function to count the number of consonants in the input string.
    
    Parameters:
    s (str): The input string to check for consonants.
    
    Returns:
    int: The count of consonants in the input string.
    """
    # Your code here
    vowels = "aeiou"
    count = 0
    for char in s.lower(): 
        # if ('a' <= char <= 'z') and char not in vowels: # OR
        if char not in vowels and char.isalnum():
            count += 1
    return count