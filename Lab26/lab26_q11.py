import numpy as np
seq="GATTACA"
encoding={'A':[1,0,0,0],'C':[0,1,0,0],'G':[0,0,1,0],'T':[0,0,0,1]}
arr=[]
for base in seq:
    arr.append(encoding[base])
result=np.array(arr)
print("DNA Sequence:",seq)
print("One hot encoding:")
print(result)