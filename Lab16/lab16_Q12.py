word=str(input("Enter a word: "))
reverse=""

for i in range(len(word)-1,-1,-1):
    reverse=reverse+word[i]
if word==reverse:
    print("Palindrome")
else:
    print("Not a palindrome")

