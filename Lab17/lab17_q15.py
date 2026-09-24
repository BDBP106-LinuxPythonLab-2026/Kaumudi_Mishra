S=input("Enter a string: ")
L=S.split()
print(L)
for word in L:
    if word.startswith("k"): print(word)