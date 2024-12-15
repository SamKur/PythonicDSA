def find_largest(numbers):
    # Check if the list is empty
    if not numbers:
        return None
 
    # Initialize the largest number as the first element
    largest = numbers[0]
    
    for num in numbers[1:]:
        # If we find a number larger than our current largest, update largest
        if num > largest:
            largest = num

    return largest
 
# Alternative solution using built-in max() function:
# def find_largest(numbers):
#     return max(numbers) if numbers else None

print(find_largest([124,3,224,52,-883, 11.009]))