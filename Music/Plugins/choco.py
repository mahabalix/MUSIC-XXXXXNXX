from pyrogram import filters, Client
from pyrogram.types import Message
from Music import app, SUDOERS, Music_START_TIME
import os
import psutil
import time
from datetime import datetime
from Music.MusicUtilities.helpers.time import get_readable_time

async def bot_sys_stats():
    bot_uptime = int(time.time() - Music_START_TIME)
    cpu = psutil.cpu_percent(interval=0.5)
    mem = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent
    stats = f'''
Uptime: {get_readable_time((bot_uptime))}
CPU: {cpu}%
RAM: {mem}%
Disk: {disk}%'''
    return stats


@app.on_message(filters.command(["mchoco", "choco"]))
async def choco(_, message):
    uptime = await bot_sys_stats()
    start = datetime.now()
    response = await message.reply_photo(
        photo="cache/pong.jpg",
        caption=">> ZPong!"
    )
    end = datetime.now()
    resp = (end - start).microseconds / 1000
    await message.edit_text(" CHOCOBAR {resp}  ..**\n#------████.   ████\n#----██.  ██^██.  ██\n#---██______s______██\n#----██______i_____██\n#-------██____m___██\n#----------██___i__██\n#-------------█████\n\nCHOCOBAR RELOADED DONE ")
    