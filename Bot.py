import discord
import asyncio
import os
import sys
import json
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
    play = discord.Game("\"번역|(요청)\"")
    await client.change_presence(status=discord.Status.online, activity=play)

@client.event
async def on_message(message):
    if message.content.startswith("번역"):
        requestedword = (message.content.split("|")[1])
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
            #json형식으로 변경
            res = json.loads(response_body.decode('utf-8'))
            from pprint import pprint
            await message.channel.send("요청하신 번역 결과는 \"" + res['message']['result']['translatedText'] + "\" 입니다")
        else:
            await message.channel.send("요청을 처리 할 수 없습니다. 개발자에게 문의해주세요 도핑#1004")


client.run(token)
