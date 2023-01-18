import firebase_admin
from firebase_admin import auth
from utility.helper import initFB

initFB()
print("Welcome to MM user deletion. To begin, enter the email you wish to delete.")
email = input()
print(f"Searching for {email}")
user = None

while user == None:
    try:
        user = auth.get_user_by_email(email)
    except firebase_admin._auth_utils.UserNotFoundError:
        print(f"{email} not found in firebase user listing")
        print("Please enter another email.")
        email = input()
print(f"Found email login for {email}")
print(f"Are you sure you want to delete user, {email} ? y/n")
decision = input()
if decision.lower() == "y":
    auth.delete_user(user.uid)
    print("User deleted!")
else:
    print("Cancelled deletion!")
