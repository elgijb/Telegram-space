import os
import random
from telegram import Bot
from dotenv import load_dotenv

def get_random_photo_path(folder):
    all_photos = [os.path.join(folder, f) for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
    if all_photos:
        return random.choice(all_photos)
    return None

def publish_text_to_channel(bot, chat_id, text):
    bot.send_message(chat_id=chat_id, text=text)

def publish_photo_to_channel(bot, chat_id, photo_path):
    with open(photo_path, 'rb') as photo:
        bot.send_photo(chat_id=chat_id, photo=photo)

if __name__ == "__main__":
    load_dotenv()

    TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
    TELEGRAM_CHANNEL_ID = os.getenv('TELEGRAM_CHANNEL_ID')

    bot = Bot(token=TELEGRAM_BOT_TOKEN)


    message = "Hello, this is a test message from my bot!"
    publish_text_to_channel(bot, TELEGRAM_CHANNEL_ID, message)


    folder = 'images'
    if not os.path.exists(folder):
        print(f"The folder '{folder}' does not exist.")
    else:
        photo_path = get_random_photo_path(folder)
        if photo_path:
            publish_photo_to_channel(bot, TELEGRAM_CHANNEL_ID, photo_path)
        else:
            print("No photos available to publish.")
