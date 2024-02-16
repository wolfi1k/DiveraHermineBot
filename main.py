import os
import dotenv
from datetime import date, datetime, timedelta
from Divera.Divera import DiveraApiClient
from Divera.Divera import DiveraMessageConverter
from Divera.Divera import News
from Hermine.main import StashCatClient


def create_divera(user: str, password: str, access_key: str):
    client = DiveraApiClient(access_key=access_key)
    client.login(user, password)
    return client

def load_news(client: DiveraApiClient):
    allNews = client.get_all_news()
    converter = DiveraMessageConverter()
    return converter.divera_news_response_to_news(allNews)


def get_news_in_three_days(news: list) -> News:
    for news_object in news:
        if news_object.is_in_three_days():
            return news_object
    return None

def create_hermine(user: str, password: str, client_key: str, encryption_key: str):
    client = StashCatClient(device_id="DiveraUpdateBot", client_key=client_key)
    hermine_login_if_necessary(client, user, password)
    client.open_private_key(encryption_key)
    return client

def hermine_login_if_necessary(client: StashCatClient, user: str, password: str):
    try:
        client.check()
    except:
        payload = client.login(user, password)
        if not payload:
            raise Error('')

def send_in_hermine(client: StashCatClient, channel_id: str, message: str) -> None:
    client.send_msg_to_channel(channel_id, message)


def main():
    dotenv.load_dotenv()
    DIVERA_USER = os.environ.get("DIVERA_USER")
    DIVERA_PASSWORD = os.environ.get("DIVERA_PASSWORD")
    DIVERA_ACCESS_KEY = os.environ.get("DIVERA_ACCESS_KEY")
    HERMINE_USER = os.environ.get("HERMINE_USER")
    HERMINE_PASSWORD = os.environ.get("HERMINE_PASSWORD")
    HERMINE_ENCRYPTION_KEY = os.environ.get("HERMINE_ENCRYPTION_KEY")
    HERMINE_CHANNEL_ID = os.environ.get("HERMINE_CHANNEL_ID")
    HERMINE_CLIENT_KEY=os.environ.get("HERMINE_CLIENT_KEY")

    divera = create_divera(DIVERA_USER, DIVERA_PASSWORD, DIVERA_ACCESS_KEY)
    news = load_news(divera)
    news_to_publish = get_news_in_three_days(news)

    if news_to_publish is None:
        return

    hermine = create_hermine(HERMINE_USER, HERMINE_PASSWORD, HERMINE_CLIENT_KEY, HERMINE_ENCRYPTION_KEY)
    send_in_hermine(hermine, HERMINE_CHANNEL_ID, news_to_publish.format())

    dotenv_path = dotenv.find_dotenv()
    dotenv.set_key(dotenv_path, "HERMINE_CLIENT_KEY", hermine.client_key)
    dotenv.set_key(dotenv_path, "DIVERA_ACCESS_KEY", divera.access_key)


if __name__ == "__main__":
    main()
