n=int(input("Enter a number: "))
def nextprime(n):
    n=n+1
    while True:
        prime=True
        for i in range(2,n):
            if n%i==0:
                prime=False
                break
        if prime:
            return n
        n=n+1
print(nextprime(n))


