from telethon.sync import TelegramClient

api_id = ''
api_hash = ''

# Create a new session or using old session
client = TelegramClient('session_name', api_id, api_hash)

async def main():
    await client.start()  # Authen the first login
    dialogs = await client.get_dialogs()
    for dialog in dialogs:
        if dialog.is_group:
            print(f"Group name: {dialog.name}, Group ID: {dialog.id}")
            # GET infomation from your group
            messages = await client.get_messages(dialog.id, limit=10)
            for message in messages:
                print(f"Message: {message.text}")

with client:
    client.loop.run_until_complete(main())
