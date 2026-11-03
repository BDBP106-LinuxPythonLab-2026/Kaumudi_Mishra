import re
text=input("Enter a piece of text: ")
pattern=r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'
emails=re.findall(pattern,text)
unique_emails=[]
for email in emails:
    if email not in unique_emails:
        unique_emails.append(email)
print("Unique email adresses are: ")
for email in unique_emails:
    print(email)