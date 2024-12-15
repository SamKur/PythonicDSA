def check_unique(lst):
    seen = set()
    for num in lst:
        if num in seen:
            return False #if num already present, program exits here
        seen.add(num)
    return True
 
print(check_unique([11, 2.0, 3, 2, 98]))