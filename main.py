import discord
import os
from keep_alive import keep_alive

intents = discord.Intents.default(
)  # You can customize this by enabling or disabling specific intents.
intents.message_content = True  # Enable access to message content (required for certain events).

client = discord.Client(intents=intents)


@client.event
async def on_ready():
  print("I'm in")
  print(client.user)


@client.event
async def on_message(message):
  if message.author != client.user and ("Hi" in message.content):
    await message.channel.send("Hi, I am Rad Bot.")


keep_alive()
token = os.environ['DISCORD_BOT_SECRET']
client.run(token)
