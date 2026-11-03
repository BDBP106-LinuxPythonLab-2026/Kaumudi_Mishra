import re
pattern=r"[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}"
line=input("Enter a csv line: ")
fields=line.split(",")
if len(fields)>3:
    email=fields[2].strip()
    if re.fullmatch(pattern, email):
        print("Third field contains an email address")
    else:
        print("Third field is not an Email address")
else:
    print("CSV must contain more than 3 fields")