import argparse
import os
import requests
from utils import download_images
from dotenv import load_dotenv

def fetch_nasa_apod(api_key, count):
    url = "https://api.nasa.gov/planetary/apod"
    params = {
        "api_key": api_key,
        "count": count
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    images = [item["url"] for item in response.json()]
    return images

if __name__ == "__main__":
    load_dotenv()

    parser = argparse.ArgumentParser(description="Fetch NASA APOD images")
    parser.add_argument('--count', type=int, default=5, help='Number of NASA ADOP images to fetch')
    args = parser.parse_args()

    api_key = os.getenv('NASA_API_KEY')
    images = fetch_nasa_apod(api_key, args.count)
    download_images(images, 'nasa_apod')
    
