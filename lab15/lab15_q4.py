# 3 September 2026
import math

a = float(input("enter a: "))
b = float(input("enter b: "))
c = float(input("enter c: "))

d = b**2-4*a*c

root1 = (-b+math.sqrt(d))/(2*a)
root2 = (-b-math.sqrt(d))/(2*a)
print("root1 is "+str(root1)+" and root2 is "+str(root2)+"")