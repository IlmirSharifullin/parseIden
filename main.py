import asyncio
import logging

from telethon import TelegramClient, events
from telethon.tl.types import UpdateNewChannelMessage

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(name)s - %(message)s')

FIND = ['16/512', 'iphone 11']
FORWARD_TO = 'dedailmir'

MAIN_CHANNEL_ID = 1767154113
TEST_CHANNEL_ID = 2079574783

API_ID = 23015942
API_HASH = '2db4a32c2fb51ff85cd473492be52642'
SESSION_NAME = 'second_acc'

client = TelegramClient(SESSION_NAME, API_ID, API_HASH)


async def new_message_handler(event: events.NewMessage.Event):
    if not isinstance(event.original_update, UpdateNewChannelMessage):
        return
    if event.original_update.message.peer_id.channel_id == TEST_CHANNEL_ID:
        text = event.original_update.message.message.lower()
        logging.info(f'MESSAGE IN TEST - {text[:20]}')
        if any(i in text for i in FIND):
            await client.forward_messages(FORWARD_TO, event.message)
    elif event.original_update.message.peer_id.channel_id == MAIN_CHANNEL_ID:
        text = event.original_update.message.message.lower()
        logging.info(f'MESSAGE IN IDEN - {text[:20]}')
        if any(i in text for i in FIND):
            await client.forward_messages(FORWARD_TO, event.message)


async def main():
    async with client:
        me = await client.get_me()
        print(me)
        client.add_event_handler(new_message_handler, events.NewMessage)
        await client.run_until_disconnected()


if __name__ == '__main__':
    asyncio.run(main())
