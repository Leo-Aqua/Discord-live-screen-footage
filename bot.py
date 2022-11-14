# This script requires the 'message_content' intent.


import discord
from mss import mss

intents = discord.Intents.default()
intents.message_content = True
token = ''
client = discord.Client(intents=intents)



@client.event
async def on_message(message):


    if message.content.startswith('!'):
       
        message = await message.channel.send('Live') 
        while True:
            mss().shot(output="foo.png")
            await message.add_files(discord.File(fp="foo.png"))
            
client.run(token)
