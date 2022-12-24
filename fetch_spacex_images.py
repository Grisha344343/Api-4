import os
import requests
from main import download_image, DIRNAME
from dotenv import load_dotenv


def fetch_spacex_last_launch(launch_id):
    url = f'https://api.spacexdata.com/v5/launches/{launch_id}'
    response = requests.get(url)
    response.raise_for_status()
    for number, link in enumerate(response.json()['links']['flickr']['original']):
        filepath = f'{DIRNAME}/{number}spacex.jpg'
        download_image(link, filepath)


if __name__ == '__main__':
    load_dotenv()
    launch_id = os.getenv("SPACEX_LAUNCH_ID", "5eb87d42ffd86e000604b384")
    fetch_spacex_last_launch(launch_id)
