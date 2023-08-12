import os
from dotenv import load_dotenv
load_dotenv()

import random
import requests

import hikari
import lightbulb
import datetime
import json
import miru

bot = lightbulb.BotApp(token=os.getenv("TOKEN"))

@bot.command
@lightbulb.command("哈囉", "天線寶寶說你好")
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx: lightbulb.Context) -> None:
    image = hikari.File('/home/heyloon-wsl/heybot/tele.jpg')
    await ctx.respond("哈囉!")
    await ctx.respond(image)

@bot.command
@lightbulb.command("time", "顯示目前時間")
@lightbulb.implements(lightbulb.SlashCommand)
async def time(ctx:lightbulb.Context) -> None:
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    await ctx.respond(f"中原標準時間:{current_time}")

@bot.command
@lightbulb.command("joke", "Sends a random Chinese joke.")
@lightbulb.implements(lightbulb.SlashCommand)
async def joke(ctx: lightbulb.Context) -> None:
    response = requests.get("https://official-joke-api.appspot.com/random_joke", verify=False)
    joke_q = response.json()["setup"]
    joke_a = response.json()["punchline"]
    await ctx.respond(joke_q)
    await ctx.respond(joke_a)

@bot.command
@lightbulb.command("waifu", "生出隨機老婆")
@lightbulb.implements(lightbulb.SlashCommand)
async def waifu(ctx: lightbulb.Context) -> None: 
    w_url = 'https://api.waifu.im/search'
    w_params = {
        'included_tags': ['maid'],
        'height': '>=2000'
    }
    response = requests.get(w_url, params=w_params)
    if response.status_code == 200:
        r_waifu = response.json()
        waifu_random = r_waifu['images'][0]['url']
        await ctx.respond(waifu_random)

bot.run()