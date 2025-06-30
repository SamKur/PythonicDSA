def printer(n):
    # iterative 
    if n <=0: return
    number = 0
    while number < n:
        number += 1
        print(number, end=' ')
printer(5)  # Output: 1 2 3 4 5


print("\nRecursive Head:")


def printer_recursive(n):
    if n <= 0: return
    printer_recursive(n-1)
    print(n, end=' ')

printer_recursive(5)  # Output: 1 2 3 4 5


print("\nRecursive Tail:")

def printer_recursive_tail(current_num, target_n):
    if current_num > target_n: return
    print(current_num, end=' ')
    printer_recursive_tail(current_num+1,target_n)

printer_recursive_tail(1,5)