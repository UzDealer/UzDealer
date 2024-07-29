import asyncio
from datetime import datetime
from telethon import TelegramClient
from telethon.tl.functions.account import UpdateProfileRequest

api_id = "26308785"
api_hash = "0bef64870d82255ba3eeb2336c73c225"
phone = "+998918113608"
session = "hour"
nick = "#UzDealer🫀" 


async def update_profile():
    client = TelegramClient(session=session, api_id=api_id, api_hash=api_hash)
    await client.start(phone=phone)

    while True:
        time = datetime.now().strftime("%H:%M")
        name = f"{nick} | {time}"
        bio = f"Hozirgi vaqt: {time}"

        await client(UpdateProfileRequest(first_name=name, about=bio))
        await asyncio.sleep(60)

try:
    asyncio.run(update_profile())
except:
    print("o'chirildi")
