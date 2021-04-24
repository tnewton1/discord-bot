import discord
import os

from dotenv import load_dotenv
load_dotenv()

token=os.getenv('TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f"{client.user} has connected to Discord.")
async def on_message(message):
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')


client.run(token)