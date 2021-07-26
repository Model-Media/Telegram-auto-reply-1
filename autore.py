from telethon import TelegramClient
import asyncio
import time
from telethon import events

api_id = '2474270'
api_hash = 'd6c0a53a212d5cd76afd69a48a9d80f8'

client = TelegramClient('Username', api_id, api_hash)

message = 'Hey, I am not available. I will come back soon. See you.
Always at your service. 🙂'

def main():

    client.start()
    
    @client.on(events.NewMessage(incoming=True))
    async def _(event):
        if event.is_private:
            time.sleep(1)  # pause for 1 second to rate-limit automatic replies
            await client.send_message(event.message.from_id, message)
    client.run_until_disconnected()


if __name__ == '__main__':
    main()
