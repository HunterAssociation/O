from pyrogram import Client, filters, enums
from pyrogram.types import *
from bot import app


@Client.on_message(filters.command("start"))
async def start(client, message):
  await message.reply("Halo !")
  answer = await message.chat.ask('*Send me your name:*', parse_mode=enums.ParseMode.MARKDOWN)
  await answer.request.edit_text("Name received!")
  await answer.reply(f'Your name is: {answer.text}', quote=True)
