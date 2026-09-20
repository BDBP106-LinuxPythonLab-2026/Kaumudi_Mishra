a=int(input("Enter length of side 1: "))
b=int(input("Enter length of side 2: "))
c=int(input("Enter length of side 3: "))
if (a+b>c) and (a+c>b) and (b+c>a):
    if a==b==c:
        print("Triangle is equilateral")
    elif a==b or b==c or c==a:
        print("Triangle is isosceles")
    else:
        print("Triangle is scalene")
else:
    print("It is not a triangle")