import os
import requests
from main import download_image, DIRNAME
from main import fetch_file_extension
from dotenv import load_dotenv


def fetch_nasa_apod(nasa_apikey, nasa_count):
    url = "https://api.nasa.gov/planetary/apod"
    payload = {"api_key": nasa_apikey, "count": nasa_count}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    for number, image in enumerate(response.json()):
        if image["media_type"] == "image":
            filepath = f'{DIRNAME}/{number}nasa.apod{fetch_file_extension(image["url"])}'
            download_image(image["url"], filepath)


if __name__ == '__main__':
    load_dotenv()
    nasa_apikey = os.getenv("NASA_APIKEY")
    nasa_count = 30
    natural_nasa = 1
    fetch_nasa_apod(nasa_apikey, nasa_count)

