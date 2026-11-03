import numpy as np

#(i)
arr_1D=np.arange(10)
print(arr_1D)

#(ii)
arr_bool=np.array([[True,False,True],[False,True,False],[True,False,True]])
print(arr_bool)

#(iii)
arr_prime=np.arange(1,51)
prime=[]
for i in arr_prime:
    if i>1:
        count=0
        for j in range(1,i+1):
            if i%j==0:
                count=count+1
        if count==2:
            prime.append(i)
prime=np.array(prime)
print(prime)

#(iv)
arr_random=np.random.rand(20)
print("1D array:")
print(arr_random)
arr_random2=arr_random.reshape(4,5)
print("2D array:")
print(arr_random2)

#(v)
a=np.arange(10)
b=np.ones(10)
c=np.hstack((a,b))
print(c)

#(vi)
a=np.arange(1,101)
b=np.array([2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97])
c=np.intersect1d(a,b)
print(c)

#(vii)
d=np.setdiff1d(a,b)
print(d)

#(viii)
indices=np.where(np.isin(a,b))
print(indices)

#(ix)
e=a[(a>5)&(a<20)]
print(e)