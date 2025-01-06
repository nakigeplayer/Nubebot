from pyrogram import Client
from pyrogram.types import Message
import extras
import moodleclient
import os

API_ID = os.getenv('API_ID')
API_HASH = os.getenv('API_HASH')
BOT_TOKEN = os.getenv('TOKEN')

bot = Client("moodle", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
data = {"moodle": "", "token": ""}

@bot.on_message()
async def messages_handler(client: Client, message: Message):
	msg = message.text
	username = message.from_user.username
	info = "Moodle: " + data["moodle"] + "\nToken: " + data["token"]
	if not username in ["ERNP05", "nakigeplayer"]:
		#await message.reply("Ke tu ase")
		return
	if msg.startswith("/start"):
		await message.reply("Moodle: " + data["moodle"] + "\nToken: " + data["token"])
	elif msg.startswith("/config"):
		try:
			m = msg.split(" ")
			data["moodle"] = m[1]
			data["token"] = m[2]
			await message.reply("Moodle: " + data["moodle"] + "\nToken: " + data["token"])
			print(data)
		except Exception as ex:
			await message.reply(ex)
	elif msg.startswith("http"):
		try:
			print(data)
			await message.reply("Procesando...")
			file = extras.download_file(msg)
			link = moodleclient.upload_token(file, data["token"], data["moodle"])
			await message.reply(link)
		except Exception as ex:
			await message.reply(ex)

bot.run()
