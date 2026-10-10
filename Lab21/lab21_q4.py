n=int(input("Enter number of terms: "))
a,b=0,1
fib=[]
for i in range(n):
    fib.append(a)
    a,b=b,a+b
odd=list(filter(lambda x: x%2!=0, fib))
print(fib)
print(odd)