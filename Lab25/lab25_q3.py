import re
pattern=r"^(00[0-9]|0[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$"
n=input("Enter a number: ")
if re.fullmatch(pattern,n):
    print("Valid")
else:
    print("Invalid")