import discord
from discord.ext import commands
import os
from googleapiclient.discovery import build
import requests
import praw
#! Import this
import random

client = commands.Bot(command_prefix="$")
api_key = "GOOGLE_SEARCH_API_KEY"

reddit = praw.Reddit(
    client_id="REDDIT_APP_ID",
    client_secret="REDDIT_APP_SECERT",
    user_agent="lol bot",
)
redditsubmission = []

@client.event
async def on_ready():
    print("!!! Bot Is Online !!!\n")
    


@client.command(aliases=["show"])
async def showpic(ctx, *, search):
    ran = random.randint(0, 9)
    resource = build("customsearch", "v1", developerKey=api_key).cse()
    result = resource.list(
        q=f"{search}", cx="SEARCH_ENGINE_ID", searchType="image"
    ).execute()
    url = result["items"][ran]["link"]
    embed1 = discord.Embed(title=f"({search.title()})")
    embed1.set_image(url=url)
    await ctx.send(embed=embed1)

@client.command("hilo")
async def hedfdfllo(ctx):
# we do not want the bot to reply to itself
    await ctx.send('hi')

@client.command("joks")
async def jdfdfokes(ctx):
    response = requests.request("GET", "https://v2.jokeapi.dev/joke/Any?format=txt")
    await ctx.send(response.text)

@client.command("mems")
async def memsddes(ctx):
    hot_posts("memes")
    for i in range(0, len(redditsubmission) - 1):
        await ctx.send(redditsubmission[i].title)
        await ctx.send(redditsubmission[i].url)
        #await message.channel.send(response.text[0:200])


def hot_posts(subreddit, lim=10):
    for submission in reddit.subreddit(subreddit).hot(limit=lim):
        redditsubmission.append(submission)
        print(submission.title)
        print(submission.url)


#client = MyClient()

client.run('DISCORD_TOKEN')
