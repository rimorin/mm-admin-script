import firebase_admin
from firebase_admin import auth
from utility.helper import initFB

READONLY_ACCESS = 1
CONDUCTOR_ACCESS = 2
ADMIN_ACCESS = 3
REMOVE_ACCESS = 0
ACCESS_LISTING = [REMOVE_ACCESS, READONLY_ACCESS, CONDUCTOR_ACCESS, ADMIN_ACCESS]

initFB()
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
claims = user.custom_claims
print(f"Found email login for {email}. Claims - {claims}")
print(
    f"Please congregation code and access level (0 - Delete claim, 1 - Read Only, 2 - Conductor, 3 - Administrator)"
)
while True:
    print("Enter code:")
    code = input()
    if claims.get(code):
        print("Claim exist.")
    access_level = -1
    while access_level not in ACCESS_LISTING:
        print("Enter access level:")
        access_value = input()
        try:
            access_level = int(access_value)
            if access_level not in ACCESS_LISTING:
                print(f"The access level {access_level} is invalid.")
        except ValueError:
            print(f"The access level {access_value} is invalid.")
    if access_level == REMOVE_ACCESS:
        claims.pop(code)
    else:
        claims[code] = access_level
    print("Do you wish to modify more claims? y/n")
    answer = input()
    if answer == "n":
        break

print(f"Configuring claims {claims} for user, {user.email}")
auth.set_custom_user_claims(user.uid, claims)
user = auth.get_user(user.uid)
print("User claims configured")
