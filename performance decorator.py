from time import time

def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f"It took {t2-t1} s.")
        return result
    return wrapper

@performance
def long_time():
    for i in range(100000000):
        i*5

long_time()

# This decorator calculates how much time is it taking to run a code.
# We can use this to test the time performance of the codes.
# Output will be like below

"""
It took 12.164413213729858 s.
"""
