from pyrogram import Client, filters, enums
from pyrogram.types import *
from bot import app


@Client.on_message(filters.command("post_season"))
async def start(client, message):
  title = await message.chat.ask('Masukkan Judul:', parse_mode=enums.ParseMode.MARKDOWN)
  studio = await message.chat.ask('Masukkan Studio:', parse_mode=enums.ParseMode.MARKDOWN)
  await message.reply(f'Judul: {title.text}\nStudio: {studio.text}')
