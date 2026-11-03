while True:
    password=input("Enter your password: ")

    upper=False
    lower=False
    digit=False
    special_ch=False

    special={"!", "@", "#", "$", "%", "&", "*"}

    for ch in password:
        if ch.isupper():
            upper=True
        if ch.islower():
            lower=True
        if ch.isdigit():
            digit=True
        if ch in special:
            special_ch=True

    validity=True

    if len(password)<8:
        print("The password must have atleast 8 characters")
        validity=False
    if not upper:
        print("The password must contain an uppercase letter")
        validity=False
    if not lower:
        print("The password must contain a lowercase character")
        validity=False
    if not digit:
        print("The password must contain a digit")
        validity=False
    if not special_ch:
        print("The password must contain a special character")
        validity=False
    if " " in password:
        print("The password must not contain a space")
        validity=False
    if "password" in password.lower():
        print("The password must not contain the word password")
        validity=False
    if validity:
        print("Password successfully generated")
        break

