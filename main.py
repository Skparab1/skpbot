import discord
import os
import time
from datetime import date
from datetime import datetime
from quadfm import quadfm
#from discord.ext import tasks

client = discord.Client()
#bot = commands.Bot(command_prefix=!)

starttimer = 0
starttimer1 = [0,0,45]
shutup = False
shutuptime = [0,0,0]
endtimer1 = [0,0,0]
elapsedtime1 = [0,0,0]

timertime = [0,0,0]
elapsedtime2 = [0,0,0]
starttimer2 = [0,0,0]
timerstarted = False
ans = 'since the bot has been restarted, ans has no value'

#if shutup and (elapsedtime1[2] >= shutuptime[2] or elapsedtime1[1] > shutuptime[1] or elapsedtime1[0] > shutuptime[0]):
  #await message.channel.send('Im back now yay')
  #shutup = False
print('Starting up...')


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

#@bot.event
#async def on_message(message):
    #if starttimer != 0:
      #elapsedtime += 1
      #await message.edit(content=elapsedtime)

def shutupwait(shutuptime,message):
  timegone = 0
  while timegone < shutuptime[0]*60*60+shutuptime[1]*60+shutuptime[2]:
    time.sleep(0.01)
    timegone += 0.01
    #message = (self.get_channel('testing').history(limit=1).flatten())[0]

    print(message.content)
    if message.content.startswith('ok you can talk now') or message.content.startswith('you can talk now'):
      break
      shutuptime = [0,0,0]

@client.event
async def on_message(message):
    print('inside loop now')
    global starttimer
    global starttimer1
    global shutup
    global shutuptime
    global endtimer1
    global ans
    global timerstarted
    global timertime
    global elapsedtime2
    global starttimer2 

    if message.channel.name == "humans":
      return

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

    if message.content.startswith('ok you can talk now') or message.content.startswith('you can talk now') or message.content.startswith('you can come back now') or message.content.startswith('ok you can come back now'):
      blank = ''
      shutuptime = [0,0,0]
      await message.channel.send('you told me to un shut up')
      await message.channel.send('yay im back now')
      elapsedtime1 = [12,60,60]
      shutup = False

    if (elapsedtime1[2] >= shutuptime[2] or elapsedtime1[1] > shutuptime[1] or elapsedtime1[0] > shutuptime[0]) and message.channel != "humans":
      try:
        if message.content.startswith('$hello'):
            await message.channel.send('Hello')
        if message.content.startswith('echo'):
            await message.channel.send(message.content.replace('echo',''))
        if message.content.startswith('whats the channel'):
            await message.channel.send(message.channel)
        if message.content.startswith('whoami'):
            await message.channel.send(message.author)
        if message.content.startswith('pingme') or message.content.startswith('ping me'):
            await message.channel.send('@'+str(message.author))
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
        if message.content.startswith('no i didnt'):
            await message.channel.send('yes you did')
        if message.content.startswith('🤛'):
            await message.channel.send('🤜')
        if message.content.startswith('🤜'):
            await message.channel.send('🤛')
        if message.content.startswith('PUT MEEEEE OUUUUUT'):
            await message.channel.send(':droplet::droplet::droplet::droplet::droplet::droplet::droplet::droplet::droplet::droplet::droplet:')
            await message.channel.send(':fire_extinguisher::fire_extinguisher::fire_extinguisher::fire_extinguisher::fire_extinguisher::fire_extinguisher::fire_extinguisher::fire_extinguisher::fire_extinguisher::fire_extinguisher::fire_extinguisher:')
        if message.content.startswith('HELP IM ON FIRE'):
            await message.channel.send('rip')
            
        if message.content.startswith('quadfm'):
            data = message.content.replace('quadfm','')
            data = data.split()
            returntxt = quadfm(data[0],data[1],data[2])

            await message.channel.send(returntxt)

        if message.content.startswith('gettable'):
           data = message.content.replace('gettable','')
           data = data.replace(' ','')
           #if 

        if message.content.startswith('yo help'):
            await message.channel.send('Commands')

            await message.channel.send('For a full list co commands go to https://github.com/Skparab1/skpbot/blob/main/README.md')

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

            elif 'hr' in shutuptimegetter or 'hours' in shutuptimegetter or 'hour' in shutuptimegetter:
              shutuptimegetter = shutuptimegetter.replace('hr','')
              shutuptimegetter = shutuptimegetter.replace('hour','')
              shutuptimegetter = shutuptimegetter.replace('hours','')
              shutuptimegetter = shutuptimegetter.replace(' ','')
              shutuptime = [int(shutuptimegetter),0,0]
              await message.channel.send('I wont talk for '+str(shutuptimegetter)+' hours')

            elif message.content.startswith('shut up forever') or message.content.startswith('shut up until i say so'):
                await message.channel.send('nooooooooooooooo-')
                shutuptime = [12,60,60]

            else:
              shutuptime = [0,0,30]
              await message.channel.send('I wont talk for 30 seconds')
            
            #shutupwait(shutuptime,message)

            #await message.channel.send('Im back now yay')

        if message.content.startswith('yo starttimer'):
            time1 = message.content.replace('yo starttimer','')
            time1 = time1.replace(' ','')

          
            dt = datetime.now()
            minute = str(int(dt.strftime("%M")))
            hour = int(dt.strftime("%H")) + 16
            second = dt.strftime("%S")
            ampm = 'AM' if int(hour) <= 12 else 'PM'
            hour = str(hour) if int(hour) <= 12 else (str(int(hour)-12))
            hour = str(hour) if int(hour) <= 12 else (str(int(hour)-12))
            starttimer2 = [hour,minute,second]

            msg = 'Timer started at '+str(hour)+':'+str(minute)+':'+str(second)+' '+ampm
            timerstarted = True
            await message.channel.send(msg)

        if message.content.startswith('yo settimer'):
          
            dt = datetime.now()
            minute = str(int(dt.strftime("%M")))
            hour = int(dt.strftime("%H")) + 16
            second = dt.strftime("%S")
            ampm = 'AM' if int(hour) <= 12 else 'PM'
            hour = str(hour) if int(hour) <= 12 else (str(int(hour)-12))
            hour = str(hour) if int(hour) <= 12 else (str(int(hour)-12))
            starttimer2 = [hour,minute,second]
            timegetter = message.content.replace('yo settimer','')

            if 'sec' in timegetter or 'seconds' in timegetter or 'second' in timegetter:
              timegetter = timegetter.replace('sec','')
              timegetter = timegetter.replace('second','')
              timegetter = timegetter.replace('seconds','')
              timegetter = timegetter.replace(' ','')
              timegetter1 = [0,0,int(timegetter)]
              await message.channel.send('Timer set for'+str(timegetter)+' seconds')

            elif 'min' in timegetter or 'minutes' in timegetter or 'minute' in timegetter:
              timegetter = timegetter.replace('min','')
              timegetter = timegetter.replace('minutes','')
              timegetter = timegetter.replace('minute','')
              timegetter = timegetter.replace(' ','')
              timegetter1 = [0,int(timegetter),0]
              await message.channel.send('Timer set for '+str(timegetter)+' minutes')

            elif 'hr' in timegetter or 'hours' in timegetter or 'hour' in timegetter:
              timegetter = timegetter.replace('hr','')
              timegetter = timegetter.replace('hour','')
              timegetter = timegetter.replace('hours','')
              timegetter = timegetter.replace(' ','')
              timegetter1 = [int(timegetter),0,0]
              await message.channel.send('Timer set for '+str(timegetter)+' hours')

            else:
              timegetter1 = [0,0,30]
              await message.channel.send('Timer set for 1 minute')

            time.sleep(timegetter1[0]*60*60+timegetter1[1]*60+timegetter1[2])
            await message.channel.send('Timer done!')

        if message.content.startswith('yo stoptimer'):

          if (timerstarted):
            timerstarted = False
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

          else:
            await message.channel.send('You need to start the timer first!')
            await message.channel.send('run yo starttimer')

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
            
            if (len(second) < 2):import discord
import os
import time
from datetime import date
from datetime import datetime
from quadfm import quadfm
#from discord.ext import tasks

client = discord.Client()
#bot = commands.Bot(command_prefix=!)

starttimer = 0
starttimer1 = [0,0,45]
shutup = False
shutuptime = [0,0,0]
endtimer1 = [0,0,0]
elapsedtime1 = [0,0,0]

timertime = [0,0,0]
elapsedtime2 = [0,0,0]
starttimer2 = [0,0,0]
timerstarted = False
ans = 'since the bot has been restarted, ans has no value'

#if shutup and (elapsedtime1[2] >= shutuptime[2] or elapsedtime1[1] > shutuptime[1] or elapsedtime1[0] > shutuptime[0]):
  #await message.channel.send('Im back now yay')
  #shutup = False
print('Starting up...')


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

#@bot.event
#async def on_message(message):
    #if starttimer != 0:
      #elapsedtime += 1
      #await message.edit(content=elapsedtime)

def shutupwait(shutuptime,message):
  timegone = 0
  while timegone < shutuptime[0]*60*60+shutuptime[1]*60+shutuptime[2]:
    time.sleep(0.01)
    timegone += 0.01
    #message = (self.get_channel('testing').history(limit=1).flatten())[0]

    print(message.content)
    if message.content.startswith('ok you can talk now') or message.content.startswith('you can talk now'):
      break
      shutuptime = [0,0,0]

@client.event
async def on_message(message):
    print('inside loop now')
    global starttimer
    global starttimer1
    global shutup
    global shutuptime
    global endtimer1
    global ans
    global timerstarted
    global timertime
    global elapsedtime2
    global starttimer2 

    if message.channel.name == "humans":
      return

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

    if message.content.startswith('ok you can talk now') or message.content.startswith('you can talk now') or message.content.startswith('you can come back now') or message.content.startswith('ok you can come back now'):
      blank = ''
      shutuptime = [0,0,0]
      await message.channel.send('you told me to un shut up')
      await message.channel.send('yay im back now')
      elapsedtime1 = [12,60,60]
      shutup = False

    if (elapsedtime1[2] >= shutuptime[2] or elapsedtime1[1] > shutuptime[1] or elapsedtime1[0] > shutuptime[0]) and message.channel != "humans":
      try:
        if message.content.startswith('$hello'):
            await message.channel.send('Hello')
        if message.content.startswith('echo'):
            await message.channel.send(message.content.replace('echo',''))
        if message.content.startswith('whats the channel'):
            await message.channel.send(message.channel)
        if message.content.startswith('whoami'):
            await message.channel.send(message.author)
        if message.content.startswith('pingme') or message.content.startswith('ping me'):
            await message.channel.send('@'+str(message.author))
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
        if message.content.startswith('no i didnt'):
            await message.channel.send('yes you did')
        if message.content.startswith('rip'):
            await message.channel.send('ikr')
        if message.content.startswith('yesss'):
            await message.channel.send('yessss!')
        if message.content.startswith('🤛'):
            await message.channel.send('🤜')
        if message.content.startswith('🤜'):
            await message.channel.send('🤛')
        if message.content.startswith('PUT MEEEEE OUUUUUT'):
            await message.channel.send(':droplet::droplet::droplet::droplet::droplet::droplet::droplet::droplet::droplet::droplet::droplet:')
            await message.channel.send(':fire_extinguisher::fire_extinguisher::fire_extinguisher::fire_extinguisher::fire_extinguisher::fire_extinguisher::fire_extinguisher::fire_extinguisher::fire_extinguisher::fire_extinguisher::fire_extinguisher:')
        if message.content.startswith('HELP IM ON FIRE'):
            await message.channel.send('rip')
            
        if message.content.startswith('quadfm'):
            data = message.content.replace('quadfm','')
            data = data.replace('ans',str(ans))
            data = data.split()
            returntxt = quadfm(data[0],data[1],data[2])

            await message.channel.send(returntxt)

        if message.content.startswith('gettable'):
          data = message.content.replace('gettable','')
          data = data.replace(' ','')
          if ',range=' in data:
            data = data.split(',range=')
            rng = data[1]
            data = data[0]
          else:
            rng = [-10,10,1]

          if 'x^2' in data:
            data = data.replace('x^2','&')
            if 'x' in data:
              data = data.replace('x','&')
              data = data.split('&')
              print(data)
              a = data[0].replace('+x','1x').replace('-x','-1x').replace('+1','1').replace('+',' ')
              if a == '':
                a = 1
              else:
                a = float(a)
              b = data[1].replace('+x','1x').replace('-x','-1x').replace('+1','1').replace('+',' ')

              if b == '':
                b = 1
              else:
                b = float(b)
              c = data[2].replace('+x','1x').replace('-x','-1x').replace('+1','1').replace('+',' ')
              if c == '':
                c = 1
              else:
                c = float(c)

              rng = rng.split(',')

              await message.channel.send('x \t f(x)')
              
              t = (a,b,c)
              await message.channel.send(t)
              for i in range(int(rng[0]),int(rng[1]),int(rng[2])):
                await message.channel.send(str(i)+'\t'+str(a*(i**2)+b*i+c))

            else:
              blank = '' #  x^2 but not x
          else:
            blank = ''  

        if message.content.startswith('🔫 hand over the eggs'):
            await message.channel.send('🥚 🥚 🥚 🥚 🥚 🥚 🥚 🥚 🥚 🥚')
      
        if message.content.startswith('yo help'):
            await message.channel.send('Commands')

            await message.channel.send('For a full list co commands go to https://github.com/Skparab1/skpbot/blob/main/README.md')

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

            elif 'hr' in shutuptimegetter or 'hours' in shutuptimegetter or 'hour' in shutuptimegetter:
              shutuptimegetter = shutuptimegetter.replace('hr','')
              shutuptimegetter = shutuptimegetter.replace('hour','')
              shutuptimegetter = shutuptimegetter.replace('hours','')
              shutuptimegetter = shutuptimegetter.replace(' ','')
              shutuptime = [int(shutuptimegetter),0,0]
              await message.channel.send('I wont talk for '+str(shutuptimegetter)+' hours')

            elif message.content.startswith('shut up forever') or message.content.startswith('shut up until i say so'):
                await message.channel.send('nooooooooooooooo-')
                shutuptime = [12,60,60]

            else:
              shutuptime = [0,0,30]
              await message.channel.send('I wont talk for 30 seconds')
            
            #shutupwait(shutuptime,message)

            #await message.channel.send('Im back now yay')

        if message.content.startswith('yo starttimer'):
            time1 = message.content.replace('yo starttimer','')
            time1 = time1.replace(' ','')

          
            dt = datetime.now()
            minute = str(int(dt.strftime("%M")))
            hour = int(dt.strftime("%H")) + 16
            second = dt.strftime("%S")
            ampm = 'AM' if int(hour) <= 12 else 'PM'
            hour = str(hour) if int(hour) <= 12 else (str(int(hour)-12))
            hour = str(hour) if int(hour) <= 12 else (str(int(hour)-12))
            starttimer2 = [hour,minute,second]

            msg = 'Timer started at '+str(hour)+':'+str(minute)+':'+str(second)+' '+ampm
            timerstarted = True
            await message.channel.send(msg)

        if message.content.startswith('yo settimer'):
          
            dt = datetime.now()
            minute = str(int(dt.strftime("%M")))
            hour = int(dt.strftime("%H")) + 16
            second = dt.strftime("%S")
            ampm = 'AM' if int(hour) <= 12 else 'PM'
            hour = str(hour) if int(hour) <= 12 else (str(int(hour)-12))
            hour = str(hour) if int(hour) <= 12 else (str(int(hour)-12))
            starttimer2 = [hour,minute,second]
            timegetter = message.content.replace('yo settimer','')

            if 'sec' in timegetter or 'seconds' in timegetter or 'second' in timegetter:
              timegetter = timegetter.replace('sec','')
              timegetter = timegetter.replace('second','')
              timegetter = timegetter.replace('seconds','')
              timegetter = timegetter.replace(' ','')
              timegetter1 = [0,0,int(timegetter)]
              await message.channel.send('Timer set for'+str(timegetter)+' seconds')

            elif 'min' in timegetter or 'minutes' in timegetter or 'minute' in timegetter:
              timegetter = timegetter.replace('min','')
              timegetter = timegetter.replace('minutes','')
              timegetter = timegetter.replace('minute','')
              timegetter = timegetter.replace(' ','')
              timegetter1 = [0,int(timegetter),0]
              await message.channel.send('Timer set for '+str(timegetter)+' minutes')

            elif 'hr' in timegetter or 'hours' in timegetter or 'hour' in timegetter:
              timegetter = timegetter.replace('hr','')
              timegetter = timegetter.replace('hour','')
              timegetter = timegetter.replace('hours','')
              timegetter = timegetter.replace(' ','')
              timegetter1 = [int(timegetter),0,0]
              await message.channel.send('Timer set for '+str(timegetter)+' hours')

            else:
              timegetter1 = [0,0,30]
              await message.channel.send('Timer set for 1 minute')

            time.sleep(timegetter1[0]*60*60+timegetter1[1]*60+timegetter1[2])
            await message.channel.send('Timer done!')

        if message.content.startswith('yo stoptimer'):

          if (timerstarted):
            timerstarted = False
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

          else:
            await message.channel.send('You need to start the timer first!')
            await message.channel.send('run yo starttimer')

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
#my_secret = os.environ['TOKEN']import discord
import os
import time
from datetime import date
from datetime import datetime
from quadfm import quadfm
#from discord.ext import tasks

client = discord.Client()
#bot = commands.Bot(command_prefix=!)

starttimer = 0
starttimer1 = [0,0,45]
shutup = False
shutuptime = [0,0,0]
endtimer1 = [0,0,0]
elapsedtime1 = [0,0,0]

timertime = [0,0,0]
elapsedtime2 = [0,0,0]
starttimer2 = [0,0,0]
timerstarted = False
ans = 'since the bot has been restarted, ans has no value'

#if shutup and (elapsedtime1[2] >= shutuptime[2] or elapsedtime1[1] > shutuptime[1] or elapsedtime1[0] > shutuptime[0]):
  #await message.channel.send('Im back now yay')
  #shutup = False
print('Starting up...')


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

#@bot.event
#async def on_message(message):
    #if starttimer != 0:
      #elapsedtime += 1
      #await message.edit(content=elapsedtime)

def shutupwait(shutuptime,message):
  timegone = 0
  while timegone < shutuptime[0]*60*60+shutuptime[1]*60+shutuptime[2]:
    time.sleep(0.01)
    timegone += 0.01
    #message = (self.get_channel('testing').history(limit=1).flatten())[0]

    print(message.content)
    if message.content.startswith('ok you can talk now') or message.content.startswith('you can talk now'):
      break
      shutuptime = [0,0,0]

@client.event
async def on_message(message):
    print('inside loop now')
    global starttimer
    global starttimer1
    global shutup
    global shutuptime
    global endtimer1
    global ans
    global timerstarted
    global timertime
    global elapsedtime2
    global starttimer2 

    if message.channel.name == "humans":
      return

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

    if message.content.startswith('ok you can talk now') or message.content.startswith('you can talk now') or message.content.startswith('you can come back now') or message.content.startswith('ok you can come back now'):
      blank = ''
      shutuptime = [0,0,0]
      await message.channel.send('you told me to un shut up')
      await message.channel.send('yay im back now')
      elapsedtime1 = [12,60,60]
      shutup = False

    if (elapsedtime1[2] >= shutuptime[2] or elapsedtime1[1] > shutuptime[1] or elapsedtime1[0] > shutuptime[0]) and message.channel != "humans":
      try:
        if message.content.startswith('$hello'):
            await message.channel.send('Hello')
        if message.content.startswith('echo'):
            await message.channel.send(message.content.replace('echo',''))
        if message.content.startswith('whats the channel'):
            await message.channel.send(message.channel)
        if message.content.startswith('whoami'):
            await message.channel.send(message.author)
        if message.content.startswith('pingme') or message.content.startswith('ping me'):
            await message.channel.send('@'+str(message.author))
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
        if message.content.startswith('no i didnt'):
            await message.channel.send('yes you did')
        if message.content.startswith('rip'):
            await message.channel.send('ikr')
        if message.content.startswith('yesss'):
            await message.channel.send('yessss!')
        if message.content.startswith('🤛'):
            await message.channel.send('🤜')
        if message.content.startswith('🤜'):
            await message.channel.send('🤛')
        if message.content.startswith('PUT MEEEEE OUUUUUT'):
            await message.channel.send(':droplet::droplet::droplet::droplet::droplet::droplet::droplet::droplet::droplet::droplet::droplet:')
            await message.channel.send(':fire_extinguisher::fire_extinguisher::fire_extinguisher::fire_extinguisher::fire_extinguisher::fire_extinguisher::fire_extinguisher::fire_extinguisher::fire_extinguisher::fire_extinguisher::fire_extinguisher:')
        if message.content.startswith('HELP IM ON FIRE'):
            await message.channel.send('rip')
            
        if message.content.startswith('quadfm'):
            data = message.content.replace('quadfm','')
            data = data.replace('ans',str(ans))
            data = data.split()
            returntxt = quadfm(data[0],data[1],data[2])

            await message.channel.send(returntxt)

        if message.content.startswith('gettable'):
          data = message.content.replace('gettable','')
          data = data.replace(' ','')
          if ',range=' in data:
            data = data.split(',range=')
            rng = data[1]
            data = data[0]
          else:
            rng = [-10,10,1]

          if 'x^2' in data:
            data = data.replace('x^2','&')
            if 'x' in data:
              data = data.replace('x','&')
              data = data.split('&')
              print(data)
              a = data[0].replace('+x','1x').replace('-x','-1x').replace('+1','1').replace('+',' ')
              if a == '':
                a = 1
              else:
                a = float(a)
              b = data[1].replace('+x','1x').replace('-x','-1x').replace('+1','1').replace('+',' ')

              if b == '':
                b = 1
              else:
                b = float(b)
              c = data[2].replace('+x','1x').replace('-x','-1x').replace('+1','1').replace('+',' ')
              if c == '':
                c = 1
              else:
                c = float(c)

              rng = rng.split(',')

              await message.channel.send('x \t f(x)')
              
              t = (a,b,c)
              await message.channel.send(t)
              for i in range(int(rng[0]),int(rng[1]),int(rng[2])):
                await message.channel.send(str(i)+'\t'+str(a*(i**2)+b*i+c))

            else:
              blank = '' #  x^2 but not x
          else:
            blank = ''  

        if message.content.startswith('🔫 hand over the eggs'):
            await message.channel.send('🥚 🥚 🥚 🥚 🥚 🥚 🥚 🥚 🥚 🥚')
      
        if message.content.startswith('yo help'):
            await message.channel.send('Commands')

            await message.channel.send('For a full list co commands go to https://github.com/Skparab1/skpbot/blob/main/README.md')

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

            elif 'hr' in shutuptimegetter or 'hours' in shutuptimegetter or 'hour' in shutuptimegetter:
              shutuptimegetter = shutuptimegetter.replace('hr','')
              shutuptimegetter = shutuptimegetter.replace('hour','')
              shutuptimegetter = shutuptimegetter.replace('hours','')
              shutuptimegetter = shutuptimegetter.replace(' ','')
              shutuptime = [int(shutuptimegetter),0,0]
              await message.channel.send('I wont talk for '+str(shutuptimegetter)+' hours')

            elif message.content.startswith('shut up forever') or message.content.startswith('shut up until i say so'):
                await message.channel.send('nooooooooooooooo-')
                shutuptime = [12,60,60]

            else:
              shutuptime = [0,0,30]
              await message.channel.send('I wont talk for 30 seconds')
            
            #shutupwait(shutuptime,message)

            #await message.channel.send('Im back now yay')

        if message.content.startswith('yo starttimer'):
            time1 = message.content.replace('yo starttimer','')
            time1 = time1.replace(' ','')

          
            dt = datetime.now()
            minute = str(int(dt.strftime("%M")))
            hour = int(dt.strftime("%H")) + 16
            second = dt.strftime("%S")
            ampm = 'AM' if int(hour) <= 12 else 'PM'
            hour = str(hour) if int(hour) <= 12 else (str(int(hour)-12))
            hour = str(hour) if int(hour) <= 12 else (str(int(hour)-12))
            starttimer2 = [hour,minute,second]

            msg = 'Timer started at '+str(hour)+':'+str(minute)+':'+str(second)+' '+ampm
            timerstarted = True
            await message.channel.send(msg)

        if message.content.startswith('yo settimer'):
          
            dt = datetime.now()
            minute = str(int(dt.strftime("%M")))
            hour = int(dt.strftime("%H")) + 16
            second = dt.strftime("%S")
            ampm = 'AM' if int(hour) <= 12 else 'PM'
            hour = str(hour) if int(hour) <= 12 else (str(int(hour)-12))
            hour = str(hour) if int(hour) <= 12 else (str(int(hour)-12))
            starttimer2 = [hour,minute,second]
            timegetter = message.content.replace('yo settimer','')

            if 'sec' in timegetter or 'seconds' in timegetter or 'second' in timegetter:
              timegetter = timegetter.replace('sec','')
              timegetter = timegetter.replace('second','')
              timegetter = timegetter.replace('seconds','')
              timegetter = timegetter.replace(' ','')
              timegetter1 = [0,0,int(timegetter)]
              await message.channel.send('Timer set for'+str(timegetter)+' seconds')

            elif 'min' in timegetter or 'minutes' in timegetter or 'minute' in timegetter:
              timegetter = timegetter.replace('min','')
              timegetter = timegetter.replace('minutes','')
              timegetter = timegetter.replace('minute','')
              timegetter = timegetter.replace(' ','')
              timegetter1 = [0,int(timegetter),0]
              await message.channel.send('Timer set for '+str(timegetter)+' minutes')

            elif 'hr' in timegetter or 'hours' in timegetter or 'hour' in timegetter:
              timegetter = timegetter.replace('hr','')
              timegetter = timegetter.replace('hour','')
              timegetter = timegetter.replace('hours','')
              timegetter = timegetter.replace(' ','')
              timegetter1 = [int(timegetter),0,0]
              await message.channel.send('Timer set for '+str(timegetter)+' hours')

            else:
              timegetter1 = [0,0,30]
              await message.channel.send('Timer set for 1 minute')

            time.sleep(timegetter1[0]*60*60+timegetter1[1]*60+timegetter1[2])
            await message.channel.send('Timer done!')

        if message.content.startswith('yo stoptimer'):

          if (timerstarted):
            timerstarted = False
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

          else:
            await message.channel.send('You need to start the timer first!')
            await message.channel.send('run yo starttimer')

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
              second = '0' + second
            

            await message.channel.send(hour+':'+minute+':'+second+' '+ampm)

      except Exception as err:
        await message.channel.send('Sorry something went wrong')
        await message.channel.send(err)

client.run(os.getenv('TOKEN'))
#my_secret = os.environ['TOKEN']