from telethon import TelegramClient
from decouple import config
import datetime

api_id = config("API_ID")
api_hash = config("API_HASH")
chat_username = config("CHAT_ID")

client = TelegramClient("session", api_id, api_hash)


async def prettify_message(message: str) -> str:

    result = " ".join([e.strip(" \n\n- ") for e in message.split()])

    return result


async def get_chat_messages() -> list:

    await client.start()
    await client.get_me()

    try:
        await client.get_dialogs()
    except ValueError:
        pass
    await client.get_entity(chat_username)

    res = [
        {
           "message": await prettify_message(message.text),
           "date": message.date.strftime("%d.%m.%y %H:%M:%S")
        }
        async for message in client.iter_messages(chat_username)
        if message.text
    ][:10]

    await client.disconnect()
    return res

