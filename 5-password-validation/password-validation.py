password = input("Enter password: ")

if len(password) < 8:
    print("Password must contain 8 characters")
elif not any(ch.isdigit() for ch in password):
    print("Password must contain a number")
elif not any(ch.isupper() for ch in password):
    print("Password must contain an uppercase letter")
elif not any(ch.islower() for ch in password):
    print("Password must contain a lowercase letter")
else:
    print("Valid Password")
