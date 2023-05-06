import pyromod
from pyrogram import Client


API_ID = "20786693"
API_HASH = "6eebbb7d9f9825a2d200c034bfbb7102"
BOT_TOKEN = "6173159110:AAFZwFeI9FpyHpfeYS81eiEeFOHFVM8o9Qs"

app = Client("Uploader", API_ID, API_HASH, bot_token=BOT_TOKEN, plugins=dict(root="Geonime"))

app.start()
