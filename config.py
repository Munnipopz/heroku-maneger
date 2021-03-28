import os

class Config:
    BOT_TOKEN = os.environ.get("1774394802:AAEJcPDc0PB0nmNQcIPJ-sk6ncPTRHJNOuA","")
    HEROKU_API_KEY = os.environ.get("1467c3d7-099f-4c99-9314-5888f59ff17d","")
    AUTHORIZED_USERS = [int(user) for user in os.environ.get("1650092910").split(" ")]
    TG_CHARACTER_LIMIT = 4000 
    HEROKU_APP_NAME = os.environ.get("herokumybot","")
