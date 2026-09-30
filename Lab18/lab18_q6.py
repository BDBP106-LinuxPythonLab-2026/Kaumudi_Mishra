a=int(input("Enter length of side a: "))
b=int(input("Enter length of side b: "))
c=int(input("Enter length of side c: "))

import math
s=(a+b+c)/2
area=math.sqrt(s*(s-a)*(s-b)*(s-c))
print(area)

#Enter length of side a: 2
#Enter length of side b: 3
#Enter length of side c: 4
#2.9047375096555625

#Enter length of side a: 12
#Enter length of side b: 13
#Enter length of side c: 23
#56.28498911788115

#Enter length of side a: 34
#Enter length of side b: 35
#Enter length of side c: 23
#373.7057666132542
