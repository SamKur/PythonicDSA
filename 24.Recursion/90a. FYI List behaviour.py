def add_item_to_list_problematic(item, my_list=[]):
    """
    Adds an item to a list. Demonstrates the problem with mutable default arguments.
    """
    my_list.append(item)
    print(f"Adding '{item}'. Current list: {my_list}")
    return my_list

print("--- Calling add_item_to_list_problematic ---")

# First call: No list provided, uses the default empty list
list1 = add_item_to_list_problematic("apple")
print(f"After first call: {list1}\n")

# Second call: Again, no list provided, expects a new empty list
list2 = add_item_to_list_problematic("banana")
print(f"After second call: {list2}\n")

# Third call: Still no list provided
list3 = add_item_to_list_problematic("cherry")
print(f"After third call: {list3}\n")

print("\n--- Observing the unexpected behavior ---")
print(f"list1 is: {list1}")
print(f"list2 is: {list2}")
print(f"list3 is: {list3}")

print(f"Are list1, list2, and list3 the same object? {list1 is list2 and list2 is list3}")




## FIX
print("\n --- FIX FIX FIX ---")




def add_item_to_list_correct(item, my_list=None):    # Note
    """
    Adds an item to a list. Correctly handles mutable default arguments.
    """
    if my_list is None:
        my_list = []  # Note: Create a new list ONLY if one wasn't provided
    
    my_list.append(item)
    print(f"Adding '{item}'. Current list: {my_list}")
    return my_list

print("\n--- Calling add_item_to_list_correct ---")

# First call
list_a = add_item_to_list_correct("grape")
print(f"After first call: {list_a}\n")

# Second call
list_b = add_item_to_list_correct("kiwi")
print(f"After second call: {list_b}\n")

# Third call
list_c = add_item_to_list_correct("mango")
print(f"After third call: {list_c}\n")

# You can also pass your own list
my_custom_list = ['orange']
list_d = add_item_to_list_correct("pear", my_custom_list)
print(f"After custom list call: {list_d}\n")
print(f"Original custom list: {my_custom_list}\n")


print("\n--- Observing the correct behavior ---")
print(f"list_a is: {list_a}")
print(f"list_b is: {list_b}")
print(f"list_c is: {list_c}")
print(f"Are list_a, list_b, and list_c the same object? {list_a is list_b and list_b is list_c}")