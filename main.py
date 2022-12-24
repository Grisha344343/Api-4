import requests
import os
from urllib.parse import urlparse
from dotenv import load_dotenv
import telegram
import random
from time import sleep


DIRNAME = "images"


def download_image(url, filepath, params=None):
    os.makedirs(DIRNAME, exist_ok=True)
    response = requests.get(url, params=params)
    response.raise_for_status()
    with open(filepath, 'wb') as file:
        file.write(response.content)


def fetch_file_extension(link):
    parsed_url = urlparse(link)
    return os.path.splitext(parsed_url.path)[1]



if __name__ == "__main__":
    load_dotenv()
    tg_token = os.getenv("TG_TOKEN")
    chat_id = os.getenv("TG_CHAT_ID")
    bot = telegram.Bot(token=tg_token)
    updates = bot.get_updates()
    filesindir = os.listdir("images")
    while True:
        filename = random.choice(filesindir)
        filepath = os.path.join("images", filename)
        with open(filepath, "rb") as photo:
            bot.send_photo(chat_id=chat_id, photo=photo.read())
        bot_delay = 86400
        sleep(bot_delay)
