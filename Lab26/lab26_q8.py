import numpy as np
arr=np.array([10,25,30,15,40,50,5,60,18,35])
print("Average:",np.mean(arr))
print("Highest:",np.max(arr))
print("Lowest:",np.min(arr))
print("Numbers above 20:", np.sum(arr>20))
print("Numbers below 20:", arr[arr<20])