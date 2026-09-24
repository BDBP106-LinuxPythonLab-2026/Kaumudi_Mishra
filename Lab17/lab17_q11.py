L=[0,2,4,3,2,4,3,5,6,7,8,9]
for i in range(len(L)):
    for j in range(i+1,len(L)):
        if L[i]==L[j]:
            print(L[i])


