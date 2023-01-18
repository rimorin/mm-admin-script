import firebase_admin
from firebase_admin import credentials
import os

SERVICE_KEY = os.environ.get("FB_SERVICE_KEY_PATH")


def initFB(db_config=None):
    firebase_admin.initialize_app(credentials.Certificate(SERVICE_KEY), db_config)
