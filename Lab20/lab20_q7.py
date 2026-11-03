text=input("Enter paragraph: ")
words=text.lower().split()
count={}
for word in words:
    word=word.strip(".,!?;:")
    if word:
        count[word]=count.get(word,0)+1
for word,c in sorted(count.items()):
    print(word,":",c)
if count:
    maximum=max(count.values())
    print("Most frequent words: ", end=" ")
for word, c in sorted(count.items()):
    if c==maximum:
        print(word,end=" ")