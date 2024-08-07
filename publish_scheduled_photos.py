import os
import random
import time
import argparse
from telegram import Bot
from dotenv import load_dotenv


def publish_photo_to_channel(bot, chat_id, photo_path):
    with open(photo_path, 'rb') as photo:
        bot.send_photo(chat_id=chat_id, photo=photo)


if __name__ == "__main__":
    load_dotenv()

    thelegram_bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
    telegram_channel_id = os.getenv('TELEGRAM_CHANNEL_ID')
    publish_interval = int(os.getenv('PUBLISH_INTERVAL', 14400))

    parser = argparse.ArgumentParser(description="Schedule photo publishing to Telegram channel.")
    parser.add_argument('--interval', type=int, default=publish_interval, help='Interval between photo publications in seconds.')
    args = parser.parse_args()

    bot = Bot(token=thelegram_bot_token)
    folder = 'images'

    published_photos = []
    
    while True:
        if not os.path.exists(folder):
            print(f"The folder '{folder}' does not exist.")
            continue

        all_files = os.walk(folder)
        for array_of_files in all_files:
            folder, nested_folder, files_names = array_of_files
            random.choice(files_names)
            for file_name in  files_names:
                photo_path = os.path.join(folder, file_name)
                publish_photo_to_channel(bot, telegram_channel_id, photo_path)
                time.sleep(5)
            time.sleep(publish_interval)