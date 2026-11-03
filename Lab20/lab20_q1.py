i=int(input("Enter a number:"))
if i>0:
    print("Positive,", end=" ")
elif i<0:
    print("Negative,", end=" ")
else:
    print("Zero")

if i!=0:
    if i%2==0:
        print("Even")
    else:
        print("Odd")

if i!=0 and i%3==0 and i%5==0:
    print("FizzBuzz number!")