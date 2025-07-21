# 1. Define the decorator function
def my_simple_decorator(func):
    def wrapper_function(*args, **kwargs): # This is the "new" function that will replace the original
        print(f"--- Calling {func.__name__} ---") # Code before the original function
        result = func(*args, **kwargs)          # Call the original function
        print(f"--- Finished {func.__name__} ---") # Code after the original function
        return result                          # Return the original function's result
    return wrapper_function # The decorator returns the new 'wrapper_function'

# 2. Apply the decorator using the '@' syntax
@my_simple_decorator
def greet(name):
    print(f"Hello, {name}!")
    return f"Greeting for {name}"

@my_simple_decorator
def add(a, b):
    print(f"Adding {a} and {b}")
    return a + b

# 3. Call the decorated functions
print("\nCalling greet:")
greet("Alice")

print("\nCalling add:")
sum_result = add(10, 5)
print(f"Sum: {sum_result}")