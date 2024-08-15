import asyncio
import logging

from telethon import TelegramClient, events
from telethon.tl.types import UpdateNewChannelMessage


logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(name)s - %(message)s')
client = TelegramClient('second_acc', 23015942, '2db4a32c2fb51ff85cd473492be52642')


async def new_message_handler(event: events.NewMessage.Event):
    if not isinstance(event.original_update, UpdateNewChannelMessage):
        return
    print(event)
    if event.original_update.message.peer_id.channel_id == 2079574783:
        logging.info('MESSAGE IN TEST')
        print(event.original_update.message.message)
        text = event.original_update.message.message
        if '16/512' in text:
            await client.forward_messages('dedailmir', event.message)

    if event.original_update.message.peer_id.channel_id == 1767154113:
        logging.info('MESSAGE IN IDEN')
        print(event.original_update.message.message)
        text = event.original_update.message.message
        if '16/512' in text:
            await client.forward_messages('dedailmir', event.message)


async def main():
    async with client:
        me = await client.get_me()
        print(me)
        client.add_event_handler(new_message_handler, events.NewMessage)
        await client.run_until_disconnected()


if __name__ == '__main__':
    asyncio.run(main())
