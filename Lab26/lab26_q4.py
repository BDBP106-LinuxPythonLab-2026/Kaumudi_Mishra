import numpy as np
arr=np.random.randint(1,100,(3,3))
print("Original matrix:")
print(arr)
arr[:,[0,1]]=arr[:,[1,0]]
print("After swapping:")
print(arr)