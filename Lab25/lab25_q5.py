import re
pattern=r"[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}"
text=input("Enter email: ")
if re.fullmatch(pattern,text):
    print("Email address found")
else:
    print("Email address not found")