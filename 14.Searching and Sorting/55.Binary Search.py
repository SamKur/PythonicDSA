def binary_search(arr, target):
    # Return the index of the first occurrence of the target
    start = 0
    end = len(arr) - 1
    result = -1  # Initialize result to -1 in case the target is not found
    
    while start <= end:
        mid = (start + end) // 2
        
        if target == arr[mid]:
            result = mid  # Update result and continue searching in the left half
            end = mid - 1
        elif target > arr[mid]:
            start = mid + 1
        else:
            end = mid - 1
    
    return result  # Return the index of the first occurrence, or -1 if not found

# arr must be sorted for Binary search
print(binary_search([10, 23, 45, 45, 50, 70, 85], 45))  # Output: 2
