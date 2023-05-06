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
  

  eps1 = (await message.chat.ask("Input Episode 1:")
    if eps1 == "-":
      None
    else:
      await message.reply(f'Judul: {title.text}\nEpisode1: {eps1.text}'))
  
  eps2 = (await message.chat.ask("Input Episode 2:")
    if eps2 == "-":
      None
    else:
      await message.reply(f'Judul: {title.text}\nEpisode1: {eps1.text}\nEpisode2: {eps2.text}'))
  
  eps3 = (await message.chat.ask("Input Episode 3:")
    if eps3 == "-":
      return
    else:
      await message.reply(f'Judul: {title.text}\nEpisode1: {eps1.text}\nEpisode2: {eps2.text}\nEpisode3: {eps3.text}'))
