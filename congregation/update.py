from firebase_admin import db
import os
from utility.constant import CONG_PATH, PROMPT_OPTIONS, YES
from utility.helper import initFB

initFB({"databaseURL": os.environ.get("RTDB_URL", "")})
cong_db_reference = db.reference(CONG_PATH)
congregations = cong_db_reference.get()
print("Welcome to MM congregation modification. Please enter the necessary details.")
print("Congregation code: ")
code = input()
code_exist = False
congregation_data = {}
while not code_exist:
    congregation_data = congregations.get(code)
    if not congregation_data:
        print("Congregation does not exist!")
        print("Please enter another congregation code.")
        code = input()
    else:
        code_exist = True
change_name = None
while change_name not in PROMPT_OPTIONS:
    existing_name = congregation_data.get("name")
    print(f"Existing name is {existing_name}. Do you wish to change it ? y/n")
    change_name = input()
    if change_name == YES:
        print("Congregation name.")
        name = input()
        congregation_data.update({"name": name})
    if change_name not in PROMPT_OPTIONS:
        print(f"Entry is invalid.")
track_race = None
existing_track_race = congregation_data.get("trackRace")
while track_race not in PROMPT_OPTIONS:
    print(
        f"Does the congregation want to track householders by their race ? (Existing value: {existing_track_race}) y/n"
    )
    track_race = input()
    if track_race not in PROMPT_OPTIONS:
        print(f"Entry is invalid.")

congregation_data.update({"trackRace": track_race == YES})
track_languages = None
existing_track_languages = congregation_data.get("trackLanguages")
while track_languages not in PROMPT_OPTIONS:
    print(
        f"Does the congregation want to track householders by their langugage ? (Existing value: {existing_track_languages}) y/n"
    )
    track_languages = input()
    if track_languages not in PROMPT_OPTIONS:
        print(f"Entry is invalid.")
congregation_data.update({"trackLanguages": track_languages == YES})
cong_db_reference.update({code: congregation_data})
print(f"Sucessfully updated congregation: {code} with {congregation_data.items()}")
