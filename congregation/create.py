import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import os
from utility.constant import CONG_PATH, PROMPT_OPTIONS, YES
from utility.helper import initFB

initFB({"databaseURL": os.environ.get("RTDB_URL", "")})
cong_db_reference = db.reference(CONG_PATH)
congregations = cong_db_reference.get()
print("Welcome to MM congregation creation. Please enter the necessary details.")
print("Congregation code: ")
code = input()
code_exist = True
while code_exist:
    if congregations.get(code):
        print("Found existing code in congregation listing!")
        print("Please enter another congregation code.")
        code = input()
    else:
        code_exist = False

print("Congregation name.")
name = input()
track_race = None
while track_race not in PROMPT_OPTIONS:
    print("Does the congregation want to track householders by their race ? y/n")
    track_race = input()
    if track_race not in PROMPT_OPTIONS:
        print(f"Entry is invalid.")

track_languages = None
while track_languages not in PROMPT_OPTIONS:
    print("Does the congregation want to track householders by their langugage ? y/n")
    track_languages = input()
    if track_languages not in PROMPT_OPTIONS:
        print(f"Entry is invalid.")

cong_db_reference.update(
    {
        code: {
            "name": name,
            "trackRace": track_race == YES,
            "trackLanguages": track_languages == YES,
        }
    }
)
print(f"Sucessfully created new congregation: {name}, with {code}")
