x1=int(input("Enter x1 value: "))
y1=int(input("Enter y1 value: "))
print(f'a=({x1},{y1})')
x2=int(input("Enter x2 value: "))
y2=int(input("Enter y2 value: "))
print(f'b=({x2},{y2})')

import math
distance=math.sqrt((x2-x1)**2+(y2-y1)**2)
print(f'Distance between a and b is {distance}')
