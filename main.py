from os.path import splitext
from typing import Dict, Any
from datetime import datetime
from time import strftime
import requests
import os
from pprint import pprint
from urllib.parse import urlparse
from dotenv import load_dotenv


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


def fetch_spacex_last_launch():
    url = 'https://api.spacexdata.com/v5/launches/5eb87d42ffd86e000604b384'
    response = requests.get(url)
    response.raise_for_status()
    for number, link in enumerate(response.json()['links']['flickr']['original']):
        filepath = f'{DIRNAME}/{number}spacex.jpg'
        download_image(link, filepath)


def fetch_nasa_apod(nasa_apikey, nasa_count):
    url = "https://api.nasa.gov/planetary/apod"
    payload = {"api_key": nasa_apikey, "count": nasa_count}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    for number, image in enumerate(response.json()):
        if image["media_type"] == "image":
            filepath = f'{DIRNAME}/{number}nasa.apod{fetch_file_extension(image["url"])}'
            download_image(image["url"], filepath)


def fetch_nasa_epic(nasa_apikey, nasa_epic_count):
    url = "https://api.nasa.gov/EPIC/api/natural/images"
    payload: dict[str, Any] = {"api_key": nasa_apikey}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    pprint(response.json())
    for number, image in enumerate(response.json()):

        datetime_date = datetime.strptime(image["date"], "%Y-%m-%d %H:%M:%S")
        formated_date = datetime_date.strftime("%Y/%m/%d")
        link = f"https://api.nasa.gov/EPIC/archive/natural/{formated_date}/png/{image['image']}.png"
        filepath = f'{DIRNAME}/{number}nasa.apod.epic.png'
        download_image(link, filepath, params=payload)


if __name__ == "__main__":
    load_dotenv()
    fetch_spacex_last_launch()
    nasa_apikey = os.getenv("NASA_APIKEY")
    nasa_epic_count = 5
    fetch_nasa_epic(nasa_apikey, nasa_epic_count)
    nasa_count = 30
    natural_nasa = 1
    fetch_nasa_apod(nasa_apikey, nasa_count)
