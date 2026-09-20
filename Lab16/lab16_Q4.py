import math
angle=float(input("Enter the angle in degrees: "))
radians=angle*math.pi/180

sin=math.sin(radians)
cos=math.cos(radians)
tan=math.tan(radians)
sec=1/math.cos(radians)
cosec=1/math.sin(radians)
cot=1/math.tan(radians)

print(f'sin: {sin:.2f}')
print(f'cos: {cos:.2f}')
print(f'tan: {tan:.2f}')
print(f'sec: {sec:.2f}')
print(f'cosec: {cosec:.2f}')
print(f'cot: {cot:.2f}')

