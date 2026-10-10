import time

def measure_time(func):
    def wrapper():
        begin=time.time()
        func()
        end=time.time()
        print("Total time taken was ",end-begin,"s")
    return wrapper

@measure_time
def population_growth():
    population=100
    for i in range(1000000):
        population=population*1.01
population_growth()