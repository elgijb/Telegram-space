import os
import requests

def get_fhile_extension(url):
    file_extension = os.path.splitext(url)[1]
    return file_extension

def download_images(image_urls, prefix):
    folder_name = 'images'
    os.makedirs(folder_name, exist_ok=True)
    for idx, url in enumerate(image_urls):
        response = requests.get(url)
        response.raise_for_status()
        file_extension = get_fhile_extension(url)
        file_name = f"{prefix}_image_{idx}{file_extension}"
        with open(os.path.join(folder_name, file_name), "wb") as file:
            file.write(response.content)