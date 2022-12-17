from typing import Dict, Any
from datetime import datetime
import requests
import os
from main import download_image, DIRNAME
from dotenv import load_dotenv


def fetch_nasa_epic(nasa_apikey, nasa_epic_count):
    url = "https://api.nasa.gov/EPIC/api/natural/images"
    payload: dict[str, Any] = {"api_key": nasa_apikey}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    for number, image in enumerate(response.json()):

        datetime_date = datetime.strptime(image["date"], "%Y-%m-%d %H:%M:%S")
        formated_date = datetime_date.strftime("%Y/%m/%d")
        link = f"https://api.nasa.gov/EPIC/archive/natural/{formated_date}/png/{image['image']}.png"
        filepath = f'{DIRNAME}/{number}nasa.apod.epic.png'
        download_image(link, filepath, params=payload)


if __name__ == "__main__":
    load_dotenv()
    nasa_apikey = os.getenv("NASA_APIKEY")
    nasa_epic_count = 5
    fetch_nasa_epic(nasa_apikey, nasa_epic_count)