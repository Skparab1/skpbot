import discord
import os
import time
from datetime import date
from datetime import datetime

client = discord.Client()


starttimer = 0
starttimer1 = [0,0,45]
shutup = False
shutuptime = [0,0,0]
endtimer1 = [0,0,0]
elapsedtime1 = [0,0,0]
ans = 'since the bot has been restarted, ans has no value'

#if shutup and (elapsedtime1[2] >= shutuptime[2] or elapsedtime1[1] > shutuptime[1] or elapsedtime1[0] > shutuptime[0]):
  #await message.channel.send('Im back now yay')
  #shutup = False

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

#@bot.event
#async def on_message(message):
    #if starttimer != 0:
      #elapsedtime += 1
      #await message.edit(content=elapsedtime)

@client.event
async def on_message(message):
    global starttimer
    global starttimer1
    global shutup
    global shutuptime
    global endtimer1
    global ans

    if message.author == client.user and message.channel != "humans":
        return


    dt = datetime.now()
    minute = str(int(dt.strftime("%M")))
    hour = int(dt.strftime("%H")) + 16
    second = dt.strftime("%S")
    ampm = 'AM' if int(hour) <= 12 else 'PM'
    hour = str(hour) if int(hour) <= 12 else (str(int(hour)-12))
    hour = str(hour) if int(hour) <= 12 else (str(int(hour)-12))
    
    endtimer1 = [hour,minute,second]
    elapsedtime1 = [int(endtimer1[0])-int(starttimer1[0]),int(endtimer1[1])-int(starttimer1[1]),int(endtimer1[2])-int(starttimer1[2])]

    if int(elapsedtime1[2]) < 0:
      elapsedtime1[2] = 60+int(elapsedtime1[2])
      elapsedtime1[1] = int(elapsedtime1[1])-1
    if int(elapsedtime1[1]) < 0:
      elapsedtime1[1] = 60+int(elapsedtime1[1])
      elapsedtime1[0] = int(elapsedtime1[0])-1

    #await message.channel.send('elapsed time'+str(elapsedtime1[0])+':'+str(elapsedtime1[1])+':'+str(elapsedtime1[2]))

    if shutup and (elapsedtime1[2] >= shutuptime[2] or elapsedtime1[1] > shutuptime[1] or elapsedtime1[0] > shutuptime[0]):
      await message.channel.send('Im back now yay')
      shutup = False

    if message.content.startswith('ok you can talk now') or message.content.startswith('you can talk now'):
      blank = ''
      #await message.channel.send('oops i did something wrong')
      shutuptime = [0,0,0]

    if (elapsedtime1[2] >= shutuptime[2] or elapsedtime1[1] > shutuptime[1] or elapsedtime1[0] > shutuptime[0]) and message.channel != "humans":
      try:
        if message.content.startswith('$hello'):
            await message.channel.send('Hello')
        if message.content.startswith('echo'):
            await message.channel.send(message.content.replace('echo',''))
        if message.content.startswith('whats the channel'):
            await message.channel.send(message.channel)
        if message.content.startswith('yo skp'):
            await message.channel.send('yo sup')
        if message.content.startswith('thats wrong'):
            await message.channel.send('oops')
        if message.content.startswith('yay'):
            await message.channel.send('yay')
        if message.content.startswith('lol'):
            await message.channel.send('haha')
        if message.content.startswith('hi'):
            await message.channel.send('hello')
        if message.content.startswith('hello'):
            await message.channel.send('hi')
        if message.content.startswith('thats correct'):
            await message.channel.send('yay')
        if message.content.startswith('good job'):
            await message.channel.send('thanks')
        if message.content.startswith('thanks'):
            await message.channel.send("you're welcome")
        if message.content.startswith('you get a'):
            await message.channel.send('yum yum')

        if message.content.startswith('whats'):
            text = message.content
            text = text.replace('whats','')
            text = text.replace(' ','')

            if 'ans' == text:
              await message.channel.send(ans)

            text = text.replace('ans',str(ans))
            if '+' in text:
              text = text.split('+')
              ans = int(text[0])+int(text[1])
              await message.channel.send(ans)
            if '-' in text:
              text = text.split('-')
              ans = int(text[0])-int(text[1])
              await message.channel.send(ans)
            if '*' in text or 'x' in text:
              text = text.replace('x','*')
              text = text.split('*')
              ans = int(text[0])*int(text[1])
              await message.channel.send(ans)
            if '/' in text:
              text = text.split('/')
              ans = int(text[0])/int(text[1])
              await message.channel.send(ans)
            if '^' in text:
              text = text.split('^')
              ans = int(text[0])**int(text[1])
              await message.channel.send(ans)

        if message.content.startswith('shut up'):
            await message.channel.send('ok :(')
            shutup = True
            dt = datetime.now()
            minute = str(int(dt.strftime("%M")))
            hour = int(dt.strftime("%H")) + 16
            second = dt.strftime("%S")
            ampm = 'AM' if int(hour) <= 12 else 'PM'
            hour = str(hour) if int(hour) <= 12 else (str(int(hour)-12))
            hour = str(hour) if int(hour) <= 12 else (str(int(hour)-12))
            starttimer1 = [hour,minute,second]
            shutuptimegetter = message.content.replace('shut up','')

            if 'sec' in shutuptimegetter or 'seconds' in shutuptimegetter or 'second' in shutuptimegetter:
              shutuptimegetter = shutuptimegetter.replace('sec','')
              shutuptimegetter = shutuptimegetter.replace('second','')
              shutuptimegetter = shutuptimegetter.replace('seconds','')
              shutuptimegetter = shutuptimegetter.replace(' ','')
              shutuptime = [0,0,int(shutuptimegetter)]
              await message.channel.send('I wont talk for '+str(shutuptimegetter)+' seconds')

            elif 'min' in shutuptimegetter or 'minutes' in shutuptimegetter or 'minute' in shutuptimegetter:
              shutuptimegetter = shutuptimegetter.replace('min','')
              shutuptimegetter = shutuptimegetter.replace('minutes','')
              shutuptimegetter = shutuptimegetter.replace('minute','')
              shutuptimegetter = shutuptimegetter.replace(' ','')
              shutuptime = [0,int(shutuptimegetter),0]
              await message.channel.send('I wont talk for '+str(shutuptimegetter)+' minutes')

            elif 'sec' in shutuptimegetter or 'seconds' in shutuptimegetter or 'second' in shutuptimegetter:
              shutuptimegetter = shutuptimegetter.replace('hr','')
              shutuptimegetter = shutuptimegetter.replace('hour','')
              shutuptimegetter = shutuptimegetter.replace('hours','')
              shutuptimegetter = shutuptimegetter.replace(' ','')
              shutuptime = [int(shutuptimegetter),0,0]
              await message.channel.send('I wont talk for '+str(shutuptimegetter)+' hours')

            elif message.content.startswith('shut up forever') or message.content.startswith('shut up until i say so'):
                await message.channel.send('nooooooooooooooo-')
                shutuptime = [12,0,0]

            else:
              shutuptime = [0,0,30]
              await message.channel.send('I wont talk for 30 seconds')
            
            timegone = 0
            while timegone < shutuptime[0]*60*60+shutuptime[1]*60+shutuptime[2]:
              time.sleep(0.01)
              timegone += 0.01
              if message.content.startswith('ok you can talk now') or message.content.startswith('you can talk now'):
                break
                shutuptime = [0,0,0]

            await message.channel.send('Im back now yay')

        if message.content.startswith('yo starttimer'):
          
            dt = datetime.now()
            minute = str(int(dt.strftime("%M")))
            hour = int(dt.strftime("%H")) + 16
            second = dt.strftime("%S")
            ampm = 'AM' if int(hour) <= 12 else 'PM'
            hour = str(hour) if int(hour) <= 12 else (str(int(hour)-12))
            hour = str(hour) if int(hour) <= 12 else (str(int(hour)-12))
            starttimer = [hour,minute,second]

            msg = 'Timer started at '+str(hour)+':'+str(minute)+':'+str(second)+' '+ampm
            await message.channel.send(msg)

        if message.content.startswith('yo stoptimer'):
          
            dt = datetime.now()
            minute = str(int(dt.strftime("%M")))
            hour = int(dt.strftime("%H")) + 16
            second = dt.strftime("%S")
            ampm = 'AM' if int(hour) <= 12 else 'PM'
            hour = str(hour) if int(hour) <= 12 else (str(int(hour)-12))
            hour = str(hour) if int(hour) <= 12 else (str(int(hour)-12))
            
            endtimer = [hour,minute,second]
            elapsedtime = [int(endtimer[0])-int(starttimer[0]),int(endtimer[1])-int(starttimer[1]),int(endtimer[2])-int(starttimer[2])]

            msg = 'Timer STOPPED at '+str(hour)+':'+str(minute)+':'+str(second)+' '+ampm
            await message.channel.send(msg)

            if int(elapsedtime[2]) < 0:
              elapsedtime[2] = 60+int(elapsedtime[2])
              elapsedtime[1] = int(elapsedtime[1])-1
            if int(elapsedtime[1]) < 0:
              elapsedtime[1] = 60+int(elapsedtime[1])
              elapsedtime[0] = int(elapsedtime[0])-1

            if (elapsedtime[0] == 0 and elapsedtime[1] == 0 and elapsedtime[2] == 0):
              msg = 'Bruh you just started it'
            elif (elapsedtime[0] == 0 and elapsedtime[1] == 0):
              msg = 'Time: '+ str(elapsedtime[2]) + ' seconds'
            elif (elapsedtime[0] == 0 and elapsedtime[2] == 0):
              msg = 'Time: '+ str(elapsedtime[1]) + ' minutes'
            elif (elapsedtime[1] == 0 and elapsedtime[2] == 0):
              msg = 'Time: '+ str(elapsedtime[0] + ' hours')
            elif (elapsedtime[0] == 0):
              msg = 'Time: '+ str(elapsedtime[1])+' minutes, '+str(elapsedtime[2])+' seconds'
            elif (elapsedtime[1] == 0):
              msg = 'Time: '+ str(elapsedtime[0])+' hours, '+str(elapsedtime[2])+' seconds'
            elif (elapsedtime[2] == 0):
              msg = 'Time: '+ str(elapsedtime[0])+' hours, '+str(elapsedtime[1])+' minutes'
            else:
              msg = 'Time: '+str(elapsedtime[0])+str(elapsedtime[1])+str(elapsedtime[2])

            await message.channel.send(msg)

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


        elif message.content.startswith('yo skp gettime 24') or message.content.startswith('whats the time 24'):
            plushour -= 8 # the 
            # its 8 hours ahead
            dt = datetime.now()
            minute = str(int(dt.strftime("%M"))+plusminute)
            if int(minute) >= 60:
              plusminute = str(int(plusminute)-60)
              hour = str(int(hour)+1)
            hour = int(dt.strftime("%H")) + plushour
            second = dt.strftime("%S")
            if hour <= 0:
              hour += 24
            hour = str(hour)

            if (len(hour) < 2):
              hour = '0' + hour
            
            if (len(minute) < 2):
              minute = '0' + minute
            
            if (len(second) < 2):
              second = '0' + second
            

            await message.channel.send(hour+':'+minute+':'+second)

        elif message.content.startswith('yo skp gettime') or message.content.startswith('whats the time'):
            plushour -= 8 # the 
            # its 8 hours ahead
            dt = datetime.now()
            minute = str(int(dt.strftime("%M"))+plusminute)
            if int(minute) >= 60:
              plusminute = str(int(plusminute)-60)
              hour = str(int(hour)+1)
            hour = int(dt.strftime("%H")) + plushour
            second = dt.strftime("%S")
            ampm = 'AM' if int(hour) <= 12 else 'PM'
            if hour <= 0:
              hour += 12
              ampm = 'PM'

            hour = str(hour) if int(hour) <= 12 else (str(int(hour)-12))

            if (len(hour) < 2):
              hour = '0' + hour
            
            if (len(minute) < 2):
              minute = '0' + minute
            
            if (len(second) < 2):
              second = '0' + second
            

            await message.channel.send(hour+':'+minute+':'+second+' '+ampm)

      except Exception as err:
        await message.channel.send('Sorry something went wrong')
        await message.channel.send(err)

client.run(os.getenv('TOKEN'))
#my_secret = os.environ['TOKEN']