from pyrogram import Client, filters
from pyrogram.types import *



@Client.on_message(filters.command("update"))
async def _update_episode(client, message):
  video = await message.chat.ask("[EPS] Pastekan link video anime nya")
  download = await message.chat.ask("[EPS] Pastekan link download anime nya")
  label = await message.chat.ask("[EPS] Pastekan Label anime nya")


  MESSAGE = """
<!-- [Thumbnail] -->


<!-- [Streaming] -->
<div id='box-movie'><div class='bixbox streaming'><div class='tvideo' id='plv'><div id='content'>
<div id='tab1'><iframe src='{video.text}' frameborder='0' allowfullscreen='yes' allow='autoplay' width='100%' height='100%'></iframe></div></div></div>
<div class='item video-nav'><div class='mobius'> <div class='iconx'>

<!-- [DOWNLOAD] -->
<a class='download' href='{download.text}'><div class='icol'><i class='fa fa-cloud-download' aria-hidden='true'></i> <span>Download</span></div></a>
<div class='icol light'><a class='pls' href='javascript:void(0);'><i class='fa fa-lightbulb-o' aria-hidden='true'></i> <span>Turn Off Light</span></a></div>
</div></div></div></div></div>
  """
  
  await message.reply(MESSAGE)
