import discord
import os
import logging
import random

logging.basicConfig(level=logging.INFO)

from dotenv import load_dotenv

load_dotenv()

token = os.getenv("TOKEN")

client = discord.Client()


@client.event
async def on_ready():
    print(f"{client.user} has connected to Discord.")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("$hello"):
        await message.channel.send("Hello!")

    message_content = message.content.lower()
    if "flip a coin" in message_content:
        rand_int = random.randint(0, 1)
        if rand_int == 0:
            results = "Heads"
        else:
            results = "Tails"
        await message.channel.send(results)
    
    if message.content.startswith("$goodbye"):
        await message.channel.send("Later, gator!")


client.run(token)
