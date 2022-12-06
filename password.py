import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth
import maskpass

# path to firebase service key json
credential = credentials.Certificate("fb-key.json")
firebase_admin.initialize_app(credential)
print(
    "Welcome to MM user password management. To begin, enter the email you wish to administer."
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
print(f"Found email login for {email}")
matched_password = False
while not matched_password:
    first_password = maskpass.askpass(prompt="Enter Password: ", mask="#")
    confirm_password = maskpass.askpass(prompt="Confirm Password: ", mask="#")
    matched_password = first_password == confirm_password
    if not matched_password:
        print("Passwords do not match. Please try again.")

auth.update_user(user.uid, password=confirm_password)
print(f"Configured password for user, {user.email}")
