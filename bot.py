import pyromod
import asyncio
from uvloop import install
from pyrogram import Client, idle


API_ID = "20786693"
API_HASH = "6eebbb7d9f9825a2d200c034bfbb7102"
BOT_TOKEN = "6173159110:AAFZwFeI9FpyHpfeYS81eiEeFOHFVM8o9Qs"

app = Client("Uploader", API_ID, API_HASH, bot_token=BOT_TOKEN, plugins=dict(root="Geonime"))


async def main():
  print("\n\n     Bot Started !")
  await app.start()
  
  await idle()
  
  print("   Bot Stopped !")
  await app.stop()
  
  
loop = asyncio.get_event_loop()
if __name__ == "__main__":
   install()
   loop.run_until_complete(main())

