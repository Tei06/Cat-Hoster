from utils import helper
import pymongo
import random
import discord
import asyncio
from utils import battleItemsSearch
mongo_url = "mongodb+srv://Tei:yeet123LMAO@shizukudb.rt4ys.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
cluster = pymongo.MongoClient(mongo_url)
db = cluster["ShizukuDB"]
collection = db['new']



def search(item):
    # turn item into lower case so it can be found in helper.py dictionary
    item = item.lower()
    items = helper.items
    found = False

    for x in items:

        # iterate through rarity (common, uncommon, rare, etc)
        for i in items[x]:

            # iterate through items inside of rarity
            if i == item:

                stats = list(items[x][i].keys())
                for c in range(len(stats)):
                    # put description in embed description and not a field

                    if stats[c] == "EMOJI":

                        emoji = items[x][i][stats[c]]
                        found = True
                        return emoji

    if not found:
        return None


def find_item_exists(item):
    item = item.lower()
    items = helper.shop_items
    found = False
    for x in items:
        for i in items[x]:
            if i == item:
                found = True
                return i
    if not found:
        return None


def check_has_item(item, user):
    hasItem = False
    for i in range(len(user["Items"])):
        for i in user["Items"][i]:
            if i == item:
                hasItem = True
                return i
    if not hasItem:
        return None


async def find_user(authorid):
    stats = collection.find_one({"_id":authorid})
    return stats

def get_user_name1(self, id):
    user = self.bot.get_user(id)
    return user.name

def get_user_name(self, id):
    user = self.bot.get_user(id)
    return user.name

def get_user_profile(self, id):
    user = self.bot.get_user(id)
    avatar = user.avatar_url
    return avatar





async def lootboxItems(ctx, authorInfo, itemRarity, authorname, item, url):
    randomItem = random.choice(list(helper.battleItems[itemRarity].keys()))
    hasItem = battleItemsSearch.check_has_item_boolean(randomItem, authorInfo)
    if hasItem:
        index = battleItemsSearch.check_has_item_index(randomItem, authorInfo)
        authorInfo["Items"][index][randomItem] += 1
        post = authorInfo
        collection.find_one_and_replace({"_id": ctx.author.id}, post)
    elif not hasItem:
        authorInfo["Items"].append({randomItem: 1})
        post = authorInfo
        collection.find_one_and_replace({"_id": ctx.author.id}, post)
    embed=discord.Embed(description = f"{authorname} opened a {item.title()} <a:dogdance:875461801180037201>", color = discord.Colour.random())
    embed.set_author(icon_url=ctx.author.avatar_url, name=f"{authorname}'s {item.title()}")
    embed.set_thumbnail(url=url)
    msg = await ctx.send(embed=embed)
    for i in range(3):
        embed=discord.Embed(description = f"{authorname} opened a {item.title()} <a:dogdance:875461801180037201>", color = discord.Colour.random())
        embed.set_author(icon_url=ctx.author.avatar_url, name=f"{authorname}'s {item.title()}")
        embed.set_thumbnail(url=url)
        await asyncio.sleep(0.4)
        await msg.edit(embed=embed)
    embed=discord.Embed(description = f'You got a {randomItem.title()}!', color = discord.Colour.random())
    embed.set_author(icon_url=ctx.author.avatar_url, name=f"{authorname}'s {item.title()}")
    await msg.edit(embed=embed)