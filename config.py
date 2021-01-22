import os

class Config:
    BOT_TOKEN = os.environ.get("1572046148:AAFggc8jpkgKoeN2uqg2MFH8OAyBIIVlTS8","")
    HEROKU_API_KEY = os.environ.get("ed4a7951-08b0-43f2-95c3-72b4a9c2c4c8","")
    AUTHORIZED_USERS = [int(user) for user in os.environ.get("1575148105").split(" ")]
    TG_CHARACTER_LIMIT = 4000 
    HEROKU_APP_NAME = os.environ.get("herokuuua","")
