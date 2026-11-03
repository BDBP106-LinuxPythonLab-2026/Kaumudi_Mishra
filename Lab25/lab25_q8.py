import re
text=input("Enter a piece of text: ")
pattern=r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'
def mask_email(match):
    email=match.group()
    parts=email.split("@")
    username=parts[0]
    domain=parts[1]
    if len(username)<=2:
        masked=username[0]+"*"*(len(username)-1)
    else:
        masked=username[0]+"*"*(len(username)-2)+username[-1]
    return masked+"@"+domain
result=re.sub(pattern,mask_email,text)
print(result)