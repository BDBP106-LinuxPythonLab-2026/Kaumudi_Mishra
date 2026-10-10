def before_after(func):
    def wrapper():
        print("Function is starting....")
        func()
        print("Function has finished!")
    return wrapper

@before_after
def calculate():
    print("Calculating...")
calculate()