from pyrogram import Client, filters
from pytgcalls import PyTgCalls
from pytgcalls.types.input_stream import AudioPiped
from yt_dlp import YoutubeDL
import os

api_id = int(os.getenv("31962477"))
api_hash = os.getenv("82862b859883481e9cc4390be4b96a5b")
bot_token = os.getenv("8727014494:AAHMyITtIJMF3Vv6of_Vf3GVbeGE8R0CnTg")

app = Client("musicbot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)
call = PyTgCalls(app)

@app.on_message(filters.command("play"))
async def play(_, message):
    if len(message.command) < 2:
        return await message.reply("❌ Song name dao")

    query = " ".join(message.command[1:])

    ydl_opts = {'format': 'bestaudio'}
    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(f"ytsearch:{query}", download=False)['entries'][0]