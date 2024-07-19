# Telegram Space Photo Publisher

Этот проект позволяет автоматически скачивать фотографии космоса из различных источников (SpaceX, NASA APOD, NASA EPIC) и публиковать их в Telegram-канале. Вы также можете настроить частоту публикаций.

## Установка

1. Клонируйте репозиторий:

    ```sh
    git clone https://github.com/ваш-репозиторий/telegram-space-photo-publisher.git
    cd telegram-space-photo-publisher
    ```

2. Создайте и активируйте виртуальное окружение:

    ```sh
    python -m venv venv
    source venv/bin/activate  # для Windows: venv\Scripts\activate
    ```

3. Установите зависимости:

    ```sh
    pip install -r requirements.txt
    ```

4. Создайте файл `.env` и заполните его вашими значениями:

    ```sh
    NASA_API_KEY=ваш_nasa_api_key
    TELEGRAM_BOT_TOKEN=ваш_telegram_bot_token
    TELEGRAM_CHANNEL_ID=@ваш_telegram_channel_id
    PUBLISH_INTERVAL=@ваш_интервал
    ```

## Скрипты

### 1. Скачивание фотографий SpaceX

Скачивает фотографии с последнего запуска SpaceX или с указанного запуска, если указан его ID.

```sh
python fetch_spacex_images.py --launch_id <launch_id>  # опционально
```

Пример:

```sh
python fetch_spacex_images.py
```

### 2. Скачивание фотографий NASA APOD

Скачивает указанное количество фотографий NASA APOD.

```sh
python fetch_nasa_apod.py --count <количество_фото>
```

Пример:

```sh
python fetch_nasa_apod.py --count 5
```

### 3. Скачивание фотографий NASA EPIC

Скачивает фотографии NASA EPIC.

```sh
python fetch_epic_images.py
```

### 4. Автоматическая публикация фотографий через заданные промежутки времени

Публикует фотографии из заданной директории через указанные промежутки времени. Если все фото были опубликованы, начинает публикацию заново, перемешав фото в случайном порядке.

```sh
python publish_scheduled_photos.py --interval <часы>
```

Пример:

```sh
python publish_scheduled_photos.py --interval 4
```

## Проверка

1. Откройте новую консоль, чтобы сбросить переменные окружения.

2. Создайте новое виртуальное окружение и активируйте его:

    ```sh
    python -m venv venv
    source venv/bin/activate  # для Windows: venv\Scripts\activate
    ```

3. Последовательно выполните все инструкции по установке и запустите каждый из скриптов, чтобы убедиться, что они работают как описано.

4. Убедитесь, что фотографии скачиваются в папку `images` и публикуются в вашем Telegram-канале.

5. Дополнительно протестируйте программу в разных режимах, чтобы убедиться в корректной работе.
