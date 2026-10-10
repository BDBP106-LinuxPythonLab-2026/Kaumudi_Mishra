def count_calls(func):
    count = 0
    def wrapper():
        nonlocal count
        count+=1
        func()
        print("Call count: ",count)
    return wrapper

@count_calls
def say_hi():
    print("Hi!")
say_hi()
say_hi()
say_hi()