#(i)
a=[i for i in range(1,51)]
total=sum([i for i in a])
print(total)
#(ii)
b=[]
b=[n for n in range(2,51) if all(n%i!=0 for i in range(2,n)) ]
print(b)
#(iii)
c=[]
for i in a:
    if i in b and i not in c:
        c.append(i)
print(c)
