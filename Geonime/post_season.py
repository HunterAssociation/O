from pyrogram import Client, filters, enums
from pyrogram.types import *
from bot import app


@Client.on_message(filters.command("post_season"))
async def start(client, message):
  title = await message.chat.ask("Input Judul:")
  synopsis = await message.chat.ask("Input Synopsis:")
  types = await message.chat.ask("Input types:")
  studio = await message.chat.ask("Input Studios:")
  premiered = await message.chat.ask("Input Premiered:")
  dateaired = await message.chat.ask("Input Date aired:")
  
  eps1 = await message.chat.ask("Input Episode 1:")
  eps2 = await message.chat.ask("Input Episode 2:")
  eps3 = await message.chat.ask("Input Episode 3:")
  
  if eps1 == "-":
    return
  else:
    await message.reply(f'Judul: {title.text}\nEpisode1: {eps1.text}')
  if eps2 == "-":
    return
  else:
    await message.reply(f'Judul: {title.text}\nEpisode1: {eps1.text}\nEpisode2: {eps2.text}')
  if eps3 == "-":
    return
  else:
    await message.reply(f'Judul: {title.text}\nEpisode1: {eps1.text}\nEpisode2: {eps2.text}\nEpisode3: {eps3.text}')
