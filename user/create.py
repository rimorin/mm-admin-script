import firebase_admin
from firebase_admin import auth
import maskpass
from utility.helper import initFB

initFB()
print("Welcome to MM user creation. Please enter the necessary details.")
print("User email: ")
email = input()
email_exist = True
while email_exist:
    try:
        auth.get_user_by_email(email)
        print("Found existing email in firebase user listing")
        print("Please enter another email.")
        email = input()
    except firebase_admin._auth_utils.UserNotFoundError:
        email_exist = False
matched_password = False
while not matched_password:
    first_password = maskpass.askpass(prompt="Enter Password: ", mask="#")
    confirm_password = maskpass.askpass(prompt="Confirm Password: ", mask="#")
    matched_password = first_password == confirm_password
    if not matched_password:
        print("Passwords do not match. Please try again.")

user = auth.create_user(email=email, password=confirm_password)
print(f"Sucessfully created new user: {user.uid}, with {email}")
