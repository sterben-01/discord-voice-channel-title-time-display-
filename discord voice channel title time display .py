import discord
import asyncio
import datetime
client = discord.Client()
distoken = "Njc2ODcwMzQ0OTU4ODAzOTgw.XkMAgA.HTyT7x9joXQLZt2sXD395IIYEr4"
# These must all be Voice Channels
timechannelUS = 677648049127817237
timechannelCN = 677648547323052052
@client.event
async def on_ready():
   print('We have logged in as {0.user}'.format(client))
   while True:
       now = datetime.datetime.now()
       NH = str(now.hour)
       NM = str(now.minute)
       BJtime = now.hour + 14
       if BJtime > 24:
           BJtime = BJtime - 24
       BH = str(BJtime)
       if now.hour < 10:
           NH = "0"+NH
       if now.minute < 10:
           NM = "0"+NM
       if BJtime < 10:
           BH = "0"+BH
       await client.get_channel(timechannelUS).edit(name=f"US {NH}:{NM}")
       await client.get_channel(timechannelCN).edit(name=f"CN {BH}:{NM}")
       await asyncio.sleep(60)
client.run(distoken)