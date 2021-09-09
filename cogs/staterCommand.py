
from os import name
from discord import embeds
import pymongo
from discord.ext import commands
import discord
from discord_slash import cog_ext, SlashContext
import asyncio
from utils import emojiSearch

mongo_url = "mongodb+srv://Tei:yeet123LMAO@shizukudb.rt4ys.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
cluster = pymongo.MongoClient(mongo_url)
db = cluster["ShizukuDB"]
collection = db['new']

mongo_urls1 = "mongodb+srv://ShizukuTest:yeet123LMAO@cluste.gmxuc.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
clusterr = pymongo.MongoClient(mongo_urls1)
db1 = clusterr["ShizukuTest"]
collec = db1['test']

mongo_urls = "mongodb+srv://brian:brianisawesome@cluster0.2tora.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
clusters = pymongo.MongoClient(mongo_urls)
dbs = clusters['ShizukuVouches']
col = dbs['Vouches']


class StarterCommand(commands.Cog):
    """basic starting commands"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def start(self, ctx, member: discord.Member = None):
        if member == None:
            stat = collection.find_one({'_id': ctx.author.id})
            user = self.bot.get_user(ctx.author.id)
            if stat == None:
                post = {
                    "_id": ctx.author.id,
                    "Balance": 0,
                    'Cats': [
                        {
                            "catID": 1,
                            "Name": f"{user.name}'s Cat",
                            "HP": 100,
                            "DEF": 20,
                            "ATK": 20,
                            "SPD": 20,
                            "Level": 1,
                            "EXP": 0,
                        }
                    ],
                    'EquipedItems': [

                    ],
                    'Items': [
                        {

                        }
                    ],
                    "Floor": [
                        {

                        }
                    ]
                }
                marriage_account = {
                    "_id": ctx.author.id,
                    "Partner": [
                        {

                        }
                    ],
                    "Name": [
                        {

                        }
                    ],
                    "Happiness Bar": [
                        {
                            
                        }
                    ],
                }
                collection.insert_one(post)
                await ctx.send("Account successfully created")
            else:
                await ctx.send("You already have an account")
        else:
            stat = collection.find_one({'_id': member.id})
            user = self.bot.get_user(member.id)
            if stat == None:
                post = {
                    "_id": member.id,
                    "Balance": 0,
                    'Cats': [
                        {
                            "catID": 1,
                            "Name": f"{user.name}'s Cat",
                            "HP": 55,
                            "DEF": 10,
                            "ATK": 10,
                            "SPD": 60,
                            "Level": 1,
                            "EXP": 0,
                        }
                    ],
                    'EquipedItems': [

                    ],
                    'Items': [

                    ],
                    "Floor": [
                        {

                        }
                    ]
                }
                collection.insert_one(post)
                await ctx.send("Account successfully created")
            else:
                await ctx.send("They already have an account")
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'pong {round(self.bot.latency * 1000)}ms')

    @commands.command()
    async def playerInfo(self, ctx):
        """gives player info"""
        stat = collection.find_one({'_id': ctx.author.id})
        catNames = []
        for i in range(len(stat['Cats'])):
            print(stat['Cats'][i])
            catNames.append(stat['Cats'][i]['Name'])
        embed = discord.Embed(title="These are your stats.")
        embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
        embed.add_field(name="Balance", value=stat['Balance'])
        await ctx.send(embed=embed)

    @ commands.command()
    async def catInfo(self, ctx):
        stat = collection.find_one({'_id': ctx.author.id})
        embed = discord.Embed(title="These are your cat's stats.")
        for i in stat['Cats'][0]:
            if i != "catID" and i != "EXP":
                embed.add_field(name=i, value=stat['Cats'][0][i])
        xpNeedForLevelUp = 100
        for i in range(stat['Cats'][0]['Level'] - 1):
            xpNeedForLevelUp = xpNeedForLevelUp * 0.05 + xpNeedForLevelUp
        try:
            # calculates percantage of blue squares
            percantage = stat['Cats'][0]['EXP'] / xpNeedForLevelUp
        except:
            print("Something went wrong calculating percantage")
            percantage = 0
        # 20 boxes * percantage = amount filled.
        boxes = int(20*percantage)

        embed.add_field(name="EXP", value=str(
            stat['Cats'][0]['EXP']) + "/" + str(xpNeedForLevelUp))
        embed.add_field(name="Progress", value=boxes * ":blue_square:" +
                        (20-boxes) * ":white_large_square:", inline = False)
        await ctx.send(embed = embed)

    @ commands.command(name = "test", description = "testing")
    async def test(self, ctx):
        embed=discord.Embed(title = "test hp bar",
                            description = "ez", color = ctx.author.color)
        msg=await ctx.send(embed = embed)
        await asyncio.sleep(1)
        hp=20
        while True:
            hp -= 4
            embed=discord.Embed(title = "test hp bar", description = "hp:" + hp * \
                                ":blue_square:" + (20-hp) * ":white_large_square:", color = ctx.author.color)
            await asyncio.sleep(1)
            await msg.edit(embed = embed)
            if hp == 0:
                break


    @ commands.command()
    async def account(self, ctx, member: discord.Member = None):
        if member == None:
            member=ctx.author
            author_stats=collection.find_one({"_id": member.id})
            await ctx.send(author_stats)
        else:
            stats=collection.find_one({"_id": member.id})
            await ctx.send(stats)

    @ commands.command()
    async def checkitem(self, ctx, member: discord.Member, *, item):
        members=collection.find_one({"_id": member.id})
        ok=emojiSearch.check_has_item(item, members)
        if ok == None:
            await ctx.send(f"{member.name} doesn't have {item}")
        elif ok != None:
            await ctx.send(f"{member.name} has {item}")

    @ commands.command()
    async def embed(self, ctx):
        embed=discord.Embed(title = "test", description = "ok")
        embed.set_thumbnail(
            url = "https://cdn.discordapp.com/attachments/884219160375214090/884245042296918056/Wooden_Bow.png")
        embed.set_image(
            url = "https://cdn.discordapp.com/attachments/884219160375214090/884245042296918056/Wooden_Bow.png")
        await ctx.send(embed = embed)
    @ commands.command(aliases = ['wipe all'])
    async def wipe_all(self, ctx):
        collec.delete_many({})
        collection.delete_many({})
        col.delete_many({})
        await ctx.send("all databases wiped")

    @ commands.command()
    async def profile(self, ctx):
        stat=collection.find_one({'_id': ctx.author.id})
        name=await emojiSearch.get_user_name(self, ctx.author.id)
        if stat == None:
            await ctx.send("You don't have an account yet.")
        else:
            embed=discord.Embed(title = f"{name}'s Profile")
            embed.set_thumbnail(
                url = "https://cdn.discordapp.com/attachments/874125145860604033/881986898720067615/grey.png")
            for i in stat['Cats'][0]:
                if i != "catID":
                    embed.add_field(name = i, value = stat['Cats'][0][i])
            await ctx.send(embed = embed)

    @ commands.command()
    async def rename(self, ctx, *, name):
        stat=collection.find_one({"_id": ctx.author.id})
        has_item=emojiSearch.check_has_item("name change ticket", stat)
        if has_item == None:
            await ctx.send("You don't have a name change ticket in your inventory")
            return
        elif has_item != None:
            item="name change ticket"
            for i in range(len(stat["Items"])):
                    if item in stat["Items"][i]:
                            stat["Items"][i][item] -= 1
                            if stat["Items"][i][item] == 0:
                                    stat["Items"].pop(i)
                                    post=stat
                                    collection.find_one_and_replace(
                                        {"_id": ctx.author.id}, post)
            oldname=stat["Cats"][0]['Name']
            stat["Cats"][0]["Name"]=name
            post=stat
            collection.find_one_and_replace({"_id": ctx.author.id}, post)
            embed=discord.Embed(title = "Rename Successful",
                                description = f"Successfully renamed <:shycat:875460456423251999> __**{oldname}**__ into __**{name}**__")
            await ctx.send(embed = embed)




def setup(bot):
    bot.add_cog(StarterCommand(bot))
