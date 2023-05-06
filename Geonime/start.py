from pyrogram import Client, filters
from pyrogram.types import *
from bot import app


@Client.on_message(filters.command("start"))
async def start(client, message):
  await message.reply("Halo !")
