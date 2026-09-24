L=[1,2,3,2,4,3,5,6,7,8,4,3,2,1]
e=2
for i in L:
    if i==e:
        L.remove(i)
print("The new list is", L)