import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth
import os

READONLY_ACCESS = 1
CONDUCTOR_ACCESS = 2
ADMIN_ACCESS = 3
ACCESS_LISTING = [READONLY_ACCESS, CONDUCTOR_ACCESS, ADMIN_ACCESS]
LANGUAGE_LISTING = ["e", "c", "b", "t", "tg", "id", "m"]


# path to firebase service key json
certfile = "fb-key.json"
if os.path.isfile(certfile):
    credential = credentials.Certificate(certfile)
    firebase_admin.initialize_app(credential)
else:
    firebase_admin.initialize_app()
print(
    "Welcome to MM user claims management. To begin, enter the email you wish to administer."
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
claims = {}
while True:
    print("Enter congregation code")
    code = input()
    access_level = -1
    while access_level not in ACCESS_LISTING:
        print("Enter access level")
        access_value = input()
        try:
            access_level = int(access_value)
            if access_level not in ACCESS_LISTING:
                print(f"The access level {access_level} is invalid.")
        except ValueError:
            print(f"The access level {access_value} is invalid.")
    claims[code] = access_level
    home_language = "unknown"
    while home_language not in LANGUAGE_LISTING:
        print("Enter home language")
        home_language = input()
        if home_language not in LANGUAGE_LISTING:
            print(f"The language {home_language} is invalid.")
    claims["homeLanguage"] = home_language
    max_tries = 0
    while max_tries < 1 or max_tries > 4:
        print("Enter maximum tries")
        max_tries_value = input()
        try:
            max_tries = int(max_tries_value)
            if max_tries < 1 or max_tries > 4:
                print(f"The maximum tries {max_tries} is invalid.")
        except ValueError:
            print(f"The maximum tries {max_tries} is invalid.")
    claims["maxTries"] = max_tries
    print("Do you wish to add more claims? y/n")
    answer = input()
    if answer == "n":
        break

print(f"Configuring claims {claims} for user, {user.email}")
auth.set_custom_user_claims(user.uid, claims)
user = auth.get_user(user.uid)
print("User claims configured")
print(user.custom_claims)
