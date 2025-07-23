# Python 3.8+ added keyword argument support to many built-in C-accelerated functions

def func(a, b, /, c, *, d, **kwargs):
    print(a, b, c, d, kwargs)

# no /      -> keyword arguments are allowed.
# /	        -> All before it = positional-only, then flexible
# *	        -> All after it = keyword-only
# *args     -> it captures extra positional ones
# **kwargs  -> it captures extra keyword ones

func(1, 2, 3, d=4, e=5)                 # Output: 1 2 3 4 {'e': 5}
func(1, 2, 3, d=4)                      # a=1, b=2, c=3, d=4, kwargs={}
func(10, 20, c=30, d=40)                # a=10, b=20, c=30, d=40, kwargs={}
func(5, 6, 7, d=8, extra=9, foo='bar')  # a=5, b=6, c=7, d=8, kwargs={'extra': 9, 'foo': 'bar'}

# NOT WORK
# func(1, 2, 3, 4)
# func(a=1, b=2, c=3, d=4)

def func2(a,b):
    print(a+b)

func2(4, b=3)   # 7


# more madness
def func3(a, b, /, c, *args, d, **kwargs): # args is variable, 
    print(f"a={a}, b={b}, c={c}, args={args}, d={d}, kwargs={kwargs}")

func3(10, 20, 30, 40, 50, d=60, x=1, y=2)
# a=10, b=20, c=30, args=(40, 50), d=60, kwargs={'x': 1, 'y': 2}