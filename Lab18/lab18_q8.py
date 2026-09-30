L=[23,32,33,44,'BDBH101','hello','python', 15, 1e-10, 'True','hit']
for i in range(0,len(L)-1,2):
    L[i],L[i+1]=L[i+1],L[i]
print(L)

#If length of list is even, range(0,len(L)-1,2)
#If length of list is odd, range(0,len(L)-2,2)