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
  if not eps1 == "-":
      await message.reply(f'Judul: {title.text}\nEpisode1: {eps1.text}')
  else None
      
  
  eps2 = await message.chat.ask("Input Episode 2:")
  if not eps2 == "-":
      await message.reply(f'Judul: {title.text}\nEpisode1: {eps1.text}\nEpisode2: {eps2.text}')
  else None
     
  
  eps3 = await message.chat.ask("Input Episode 3:")
  if not eps3 == "-":
      await message.reply(f'Judul: {title.text}\nEpisode1: {eps1.text}\nEpisode2: {eps2.text}\nEpisode3: {eps3.text}')
  else None
      
