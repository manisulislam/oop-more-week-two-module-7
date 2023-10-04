import math
def timer(func):
    def inner(*args, **kargs):
        print("inner started")
        # print(func)
        func(*args, **kargs)
        print("inner ended")
    return inner

# timer()()
#
@timer
def get_factorial(n):
    print("factorial starting..")
    result= math.factorial(n)
    print(f"factorial of {n} is {result}")

# timer(get_factorial)()
get_factorial(5)