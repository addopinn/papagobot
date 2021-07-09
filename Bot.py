import discord
import asyncio
import os
import sys
import urllib.request
import datetime
from Dtime import Uptime
client = discord.Client()
Uptime.uptimeset()
token = "ODYyOTU4MDI5Mjc5MzMwMzI1.YOf6Sw.iAKfZ0OrKqbLHEwONMT2m1DxAa0"


@client.event
async def on_ready():
    print(client.user.name)
    print(client.user.id)
    print('로그인 완료')
    print("="*50)
    play = discord.Game("번역")
    await client.change_presence(status=discord.Status.online, activity=play)

@client.event
async def on_message(message):
    if message.content.startswith("번역"):
        requestedword = (message.content.split("|")[1])
        await message.channel.send(requestedword)
        print(requestedword)
        client_id = "S4q2pSWjiAd9od7msSU5" # 개발자센터에서 발급받은 Client ID 값
        client_secret = "6grdOfrbwz" # 개발자센터에서 발급받은 Client Secret 값
        encText = urllib.parse.quote(requestedword)
        data = "source=ko&target=en&text=" + encText
        url = "https://openapi.naver.com/v1/papago/n2mt"
        request = urllib.request.Request(url)
        request.add_header("X-Naver-Client-Id",client_id)
        request.add_header("X-Naver-Client-Secret",client_secret)
        response = urllib.request.urlopen(request, data=data.encode("utf-8"))
        rescode = response.getcode()
        if(rescode==200):
            response_body = response.read() 
            print(response_body.decode('utf-8'))
            await message.channel.send(response_body.decode('utf-8'))

client.run(token)
