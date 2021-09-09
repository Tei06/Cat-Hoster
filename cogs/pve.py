from os import name
from types import coroutine
from discord import colour
import pymongo
import discord
from discord.ext import commands
import random
import asyncio
from cogs import catexp 
from utils import emojiSearch

#enemy
mongo_urls = "mongodb+srv://brian:brianisawesome@cluster0.2tora.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
clusters = pymongo.MongoClient(mongo_urls)
dbs = clusters['ShizukuVouches']
col = dbs['Vouches']

mongo_url = "mongodb+srv://Tei:yeet123LMAO@shizukudb.rt4ys.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
cluster = pymongo.MongoClient(mongo_url)
db = cluster["ShizukuDB"]
collection = db['new']


class Pve(commands.Cog):
    """fight against bots i guess"""
    def __init__(self, bot):
        self.bot = bot

    

    @commands.command()
    async def wipe(self, ctx):
        col.delete_many({})
        await ctx.send("database wiped")

    @commands.command()
    async def wipe2(self, ctx):
        collection.delete_many({})
        await ctx.send("database wiped")

def setup(bot):
    bot.add_cog(Pve(bot))
