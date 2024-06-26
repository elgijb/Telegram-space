import os
import random
import time
import argparse
from telegram import Bot
from dotenv import load_dotenv
from publish_text import get_random_photo_path

def publish_photo_to_channel(bot, chat_id, photo_path):
    with open(photo_path, 'rb') as photo:
        bot.send_photo(chat_id=chat_id, photo=photo)

if __name__ == "__main__":
    load_dotenv()

    TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
    TELEGRAM_CHANNEL_ID = os.getenv('TELEGRAM_CHANNEL_ID')
    PUBLISH_INTERVAL = int(os.getenv('PUBLISH_INTERVAL', 14400))

    parser = argparse.ArgumentParser(description="Schedule photo publishing to Telegram channel.")
    parser.add_argument('--interval', type=int, default=PUBLISH_INTERVAL, help='Interval between photo publications in seconds.')
    args = parser.parse_args()

    bot = Bot(token=TELEGRAM_BOT_TOKEN)
    folder = 'images'

    published_photos = []
    
    while True:
        if not os.path.exists(folder):
            print(f"The folder '{folder}' does not exist.")
        else:
            all_photos = [os.path.join(folder, f) for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
            if not all_photos:
                print("No photos available to publish.")
            else:
                if len(published_photos) == len(all_photos):
                    published_photos = []

                remaining_photos = list(set(all_photos) - set(published_photos))
                photo_path = random.choice(remaining_photos)
                publish_photo_to_channel(bot, TELEGRAM_CHANNEL_ID, photo_path)
                published_photos.append(photo_path)

                print(f"Published photo: {photo_path}")
                
        time.sleep(args.interval)
