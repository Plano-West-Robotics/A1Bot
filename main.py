import os
import discord
from discord.ext import commands
from discord.utils import find
#from keep_alive import keep_alive

token = os.environ['TOKEN']

intents = discord.Intents.all()
intents.members = True
intents.message_content = True
intents.typing = False
intents.presences = False
intents.reactions = True

#client = discord.Client(intents=intents)
client = commands.Bot(command_prefix='$', activity = discord.Game(name="$help"), intents=intents)

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message): 
  if message.author == client.user:
    return 

'''
  if message.content == prefix+'help':
    await message.channel.send('Hi! I am A1Bot, this year\'s robot for Free of            Charge#14523! These are a list of commands I can use: ')

  if message.content == 'onh':
    await message.add_reaction('\U0001F451')
'''

#keep_alive()
client.run(token)