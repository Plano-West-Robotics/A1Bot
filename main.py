import os
import discord
from keep_alive import keep_alive

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
prefix = os.environ['PREFIX']

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message): 
  if message.author == client.user:
    return 

  if message.content == prefix+'help':
    await message.channel.send('Hi! I am A1Bot, this year\'s robot for Free of            Charge#14523! These are a list of commands I can use: ')

  if message.content == 'onh':
    await message.add_reaction('\U0001F451')

keep_alive()
client.run(os.environ['TOKEN'])