import numpy as np
def maximum(a,b):
    c=np.maximum(a,b)
    return c
a=np.array([1,2])
b=np.array([0,5])
c=maximum(a,b)
print(c)