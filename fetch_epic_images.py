import requests
import os
import argparse
from dotenv import load_dotenv
from utils import download_images


def fetch_epic_images(api_key):
    url = "https://api.nasa.gov/EPIC/api/natural/images"
    params = {
        "api_key": api_key
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    images = response.json()
    image_urls = []
    for image in images:
        date = image['date'].split()[0].replace('-', '/')
        image_name = image['image']
        image_urls.append(f"https://epic.gsfc.nasa.gov/archive/natural/{date}/png/{image_name}.png")
    return image_urls

if __name__ == "__main__":
    load_dotenv()

    parser = argparse.ArgumentParser(description="Fetch NASA EPIC images")
    args = parser.parse_args()

    api_key = os.getenv('NASA_API_KEY')
    images = fetch_epic_images(api_key)
    download_images(images, 'nasa_epic')