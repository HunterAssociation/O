from pyrogram import Client, filters
from pyrogram.types import *
from bot import app


@app.on_message(filters.command("start"))
async def start(client, message):
  await message.reply("Halo !")
