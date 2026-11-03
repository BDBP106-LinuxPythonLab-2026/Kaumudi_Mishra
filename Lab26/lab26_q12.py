import numpy as np
arr=np.random.rand(5,10)*100
print("Original gene expression:")
print(arr)
mean=np.mean(arr,axis=1,keepdims=True)
normalized=arr-mean
print("Normalized expression:")
print(normalized)
sample_sum=np.sum(normalized,axis=0)
print("Sample sums:")
print(sample_sum)
threshold=50
print("Samples above threshold:")
print(np.where(sample_sum>threshold)[0]+1)