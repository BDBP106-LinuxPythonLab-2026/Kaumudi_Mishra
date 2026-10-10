import time
import math

def measure_time(func):
    def wrapper(n):
        begin=time.time()
        func(n)
        end=time.time()
        print("Total time taken was ",end-begin,"s")
    return wrapper

@measure_time
def factorial(n):
    print("Factorial of",n, "is", math.factorial(n))
factorial(50)