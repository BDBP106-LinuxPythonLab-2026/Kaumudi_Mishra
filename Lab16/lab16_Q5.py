import math
a=float(input("Enter a: "))
b=float(input("Enter b: "))
c=float(input("Enter c: "))

d=b**2-4*a*c

if (d<0):
    print("discriminant is negative, so no roots found")
    print(f'discrimnant is {d}')
else:
    root1=(-b+math.sqrt(d))/(2*a)
    root2=(-b-math.sqrt(d))/(2*a)
    print(f'root1 is {root1}')
    print(f'root2 is {root2}')