L=[1,5,6,2,3,2,4,5,6,7,5]
k=2
for x in L:
    if L.count(x)>k:
        print(x)
        break