import discord
import os
import scraper
from alive import keep_alive




myGroup = scraper.myGroup()
print(myGroup)
client = discord.Client()


@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.content.startswith('!hello'):
    await message.channel.send('Hello!')

  if message.content.startswith('!rank'):
    await message.channel.send(scraper.printGroup(scraper.myGroup()))

  if message.content.startswith('!search'):
    s = (message.content).split()
    print(int(s[1]))
    await message.channel.send(scraper.printGroup(scraper.search(int(s[1]))))
    
keep_alive()

try:
  client.run(os.environ['TOKEN'])
except:
  os.system("kill 1")
  


