import firebase_admin
from firebase_admin import auth
from utility.helper import initFB

initFB()
print(
    "Welcome to MM user details management. To begin, enter the email you wish to administer."
)
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
print(
    f"Found email login for {email}. Details - name: {user.display_name}, email_verified: {user.email_verified}"
)
print("Enter name:")
name = input()
print("Is this user's email verified? y/n")
answer = input()
auth.update_user(user.uid, email_verified=(answer.lower() == "y"), display_name=name)
user = auth.get_user(user.uid)
print(
    f"User details updated! Name: {user.display_name}, email_verified: {user.email_verified}"
)
