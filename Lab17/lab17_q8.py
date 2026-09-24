S=input("Enter a sentence: ")
W=input("Enter a word: ")
words=S.split()
count=0
for word in words:
    if word==W:
        count=count+1
print(count)