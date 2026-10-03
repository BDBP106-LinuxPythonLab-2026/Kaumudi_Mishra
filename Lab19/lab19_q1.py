#(i)
a=[i for i in range(1,51)]
print(a)
#(ii)
b=a[1:5]
print("a[1:5] is:",b)
c=a[3:20:2]
print("a[3:20:2] is:",c)
d=a[::2]
print("a[::2] is:",d)
e=a[::]
print("a[::] is:",e)
f=a[10::2]
print("a[10::2] is:",f)
g=a[1:1:1]
print("a[1:1:1] is:",g)
h=a[:0:]
print("a[:0:] is:",h)
i=a[-7::1]
print("a[-7::1] is:",i) #No, the output is not an empty list as it starts from the end of the list and goes till the -7th index and then until the last element it is increased by a step of 1.
j=a[-6:]
print("a[-6:] is:",j)
h=a[-10:-4]
print("a[-10:-4] is:",h)
#(iii)
i=a[::-1]
print("a[::-1] is:",i)
j=a[::-3]
print("a[::-3] is:",j)
k=a[:1:-2]
print("a[:1:-2] is:",k)
l=a[-1:-1:-1]
print("a[-1:-1:-1] is:",l)
m=a[:-5:-1]
print("a[:-5:-1] is:",m)
n=a[:0:-1]
print("a[:0:-1] is:",n)
o=a[:-1:-1]
print("a[:-1:-1] is:",o)
p=a[0:-5:-1]
print("a[0:-5:-1] is:",p)
q=a[-1:5:-1]
print("a[-1:5:-1] is:",q)
r=a[2:2:-1]
print("a[2:2:-1] is:",r)
s=a[2:1:-1]
print("a[2:1:-1] is:",s)
t=a[0:-5]
print("a[0:-5] is:",t)
#(iv)
even=a[1::2]
print("list of even numbers from a is:",even)
l1=a[:10]
l2=a[35::2]
l1.extend(l2)
print(l1)