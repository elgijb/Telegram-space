import argparse
import requests
from dotenv import load_dotenv
from utils import download_images


def fetch_spacex_images(launch_id):
    url = f"https://api.spacexdata.com/v4/launches/{launch_id}"
    response = requests.get(url)
    response.raise_for_status()
    images = response.json()["links"]["flickr"]["original"]
    return images



if __name__ == "__main__":
    load_dotenv()

    parser = argparse.ArgumentParser(description="Fetch SpaceX images by launch ID.")
    parser.add_argument('--launch_id', type=str, default='5eb87d47ffd86e000604b38a', help='ID of SpaceX launch')
    args = parser.parse_args()

    images = fetch_spacex_images(args.launch_id)
    
    download_images(images, 'spacex')