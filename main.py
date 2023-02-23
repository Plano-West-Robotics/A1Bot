import os
import discord
from discord.ext import commands
from discord.utils import find
from keep_alive import keep_alive
import re

token = os.environ['TOKEN']

intents = discord.Intents.all()
intents.members = True
intents.message_content = True
intents.typing = False
intents.presences = False
intents.reactions = True

onh_re = r"(?i)( |^)onh( |$)"
jasper_re = r"(?i)( |^)jasper( |$)"

#client = discord.Client(intents=intents)
client = commands.Bot(command_prefix='$', activity = discord.Game(name="$help"), intents=intents)
client.remove_command('help')

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message): 
  if message.author == client.user:
    return 
  if re.search(onh_re, message.content):
    await message.add_reaction('\U0001F451')
  #announcements id & Hemanth967#8456 id
  if message.channel.id == 995913953542668328 and message.author.id == 526054276355850266:
    await message.add_reaction('\U0001F1F4')
    await message.add_reaction('\U0001F1F3')
    await message.add_reaction('\U0001F1ED')
    await message.add_reaction('\U0001F451')
  if re.search(jasper_re, message.content):
    await message.add_reaction('\U0001F40D')
  # process commands
  await client.process_commands(message)

@client.command()
async def help(ctx):
  await ctx.send('Hi! I am A1Bot, this year\'s robot for Free of Charge#14523! These are a list of commands I can use: ')

keep_alive()
client.run(token)
