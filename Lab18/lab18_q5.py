s=input("Enter a sentence: ")
words=s.split()
d={}
for word in words:
    d[word]=1
unique=set(words)
for word in words:
    if word in unique:
        print(word,end=" ")
        unique.remove(word)
