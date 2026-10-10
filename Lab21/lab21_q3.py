import math
angles=(0,30,45,60,90)
result=list(map(lambda x: (math.sin(math.radians(x)), math.cos(math.radians(x))), angles))
print(result)