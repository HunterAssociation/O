from pyrogram import Client, filters, enums
from pyrogram.types import *
from bot import app


@Client.on_message(filters.command("post_season"))
async def start(client, message):
  title = await message.chat.ask('Masukkan Judul:')
  studio = await message.chat.ask('Masukkan Studio:')
  await message.reply(f'Judul: {title.text}\nStudio: {studio.text}')
