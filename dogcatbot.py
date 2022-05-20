from http import client
from tokenize import Token
import discord
import requests

TOKEN = "cut it ;)"

class YLBotClient(discord.Client):
    async def on_message(self, message):
        if message.author == self.user:
            return
        elif "cat" in message.content.lower():
            res = requests.get("https://api.thecatapi.com/v1/images/search%22).json()
            await message.channel.send(res[0]["url"])
        elif "dog" in message.content.lower():
            res = requests.get("https://dog.ceo/api/breeds/image/random%22).json()
            await message.channel.send(res["message"])

intents = discord.Intents.default()
intents.members = True
client = YLBotClient(intents=intents)
client.run(TOKEN)
