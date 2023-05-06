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
  if eps1 == "-":
    xep1 = ""
  else:
    xep1 = f"eps: {eps1}"
    await message.reply(xeps1.text)
