import discord
import os
from datetime import date
from datetime import datetime

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('yo skp getdate') or message.content.startswith('whats the date'):
        dt = date.today()
        dt = dt.strftime("%B %d, %Y")
        await message.channel.send(dt)

    plushour = 0
    plusminute = 0

    if message.content.startswith('yo skp gettime austin') or message.content.startswith('yo skp gettime austin,tx'):
      plushour = 2
        

    if message.content.startswith('yo skp gettime new york') or message.content.startswith('yo skp gettime ny'):
        plushour = 3

    if message.content.startswith('yo skp gettime mumbai') or message.content.startswith('yo skp gettime mumbai,india'):
        plushour = 13
        plusminute = 30

    if message.content.startswith('yo skp gettime beijing') or message.content.startswith('yo skp gettime beijing,china'):
        plushour = 16
        
    if message.content.startswith('yo skp gettime') or message.content.startswith('whats the time'):
        plushour -= 8
        dt = datetime.now()
        minute = str(int(dt.strftime("%M"))+plusminute)
        if int(minute) >= 60:
          plusminute = str(int(plusminute)-60)
          hour = str(int(hour)+1)
        hour = int(dt.strftime("%H")) + plushour
        second = dt.strftime("%S")
        ampm = 'AM' if int(hour) <= 12 else 'PM'
        hour = str(hour) if int(hour) <= 12 else (str(int(hour)-12))

        if (len(hour) < 2):
          hour = '0' + hour
        
        if (len(minute) < 2):
          minute = '0' + minute
        
        if (len(second) < 2):
          second = '0' + second
        

        await message.channel.send(hour+':'+minute+':'+second+' '+ampm)

client.run(os.getenv('TOKEN'))