def check_positive(func):
    def wrapper(n):
        if n>0:
            func(n)
        else:
            print("Number must be positive")
    return wrapper

@check_positive
def display(n):
    print(n)

display(5)
display(-23)
display(7)