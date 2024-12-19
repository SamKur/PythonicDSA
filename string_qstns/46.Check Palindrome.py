def is_palindrome(s):
    """
    Function to check if the input string is a palindrome.
    
    Parameters:
    s (str): The input string to check.
    
    Returns:
    bool: True if the string is a palindrome, False otherwise.
    """
    # Your code here
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789'
    s = s.lower()
    s = ''.join(char for char in s if char.isalnum())
    return s==s[::-1]