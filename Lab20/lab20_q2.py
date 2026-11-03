text=input("Enter text:")

vowels=0
consonants=0
digits=0
spaces=0

for ch in text.lower():
    if ch in "aeiou":
        vowels+=1
    elif ch.isalpha():
        consonants+=1
    elif ch.isdigit():
        digits+=1
    elif ch==" ":
        spaces+=1

print("Vowels:",vowels, end=" ")
print("Consonants:",consonants, end=" ")
print("Digits:",digits, end=" ")
print("Spaces:",spaces, end=" ")

