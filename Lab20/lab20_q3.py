secret=25
attempts=0

while True:
    guess=int(input("Enter a number:"))
    attempts+=1
    if guess==secret:
        print("Secret Number found, attempts took were:",attempts)
        break
    elif guess>secret:
        print("Too high")
    else:
        print("Too low")
    if attempts==7:
        print("The secret number was:",secret)
        break

