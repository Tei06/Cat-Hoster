
import random
from discord import emoji
import asyncio
from discord.ext import commands
import pymongo
import discord
from utils import helper, emojiSearch, battleItemsSearch
import math
from collections import Counter
from datetime import datetime


# user db
mongo_url = "mongodb+srv://Tei:yeet123LMAO@shizukudb.rt4ys.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
cluster = pymongo.MongoClient(mongo_url)
db = cluster["ShizukuDB"]
collection = db['new']

# item db
mongo_urls1 = "mongodb+srv://ShizukuTest:yeet123LMAO@cluste.gmxuc.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
clusterr = pymongo.MongoClient(mongo_urls1)
db1 = clusterr["ShizukuTest"]
collec = db1['test']

# TODO:
# set up user inventory using db
# trading commands
# make shop purchase command


class Items(commands.Cog):
    """cat item system"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def shop(self, ctx, *page):
        if len(page) != 0:
            page = page[0]
        else:
            page = "1"
        if page == "1":
            embed = discord.Embed(
                title="Cat Merchant's Market: Special Traits",
                description="All traits cost __**5000**__ gold, players can equip `2` traits onto their character.")
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/881990844226367531/882011191571017828/d6eo11s-c5758f3b-b486-4c49-9183-f56247fa7f7e.gif")
            embed.set_footer(
                text="page 1/4", icon_url="https://cdn.discordapp.com/attachments/881990844226367531/882013336726802453/a1ea1a79459efaa.png")
            shop_items = helper.shop_items
            for x in shop_items:
                if x == "Traits":
                    for i in shop_items[x]:
                        stats = list(shop_items[x][i].keys())
                        for c in range(len(stats)):
                            if stats[c] == "DESCRIPTION":
                                decs = shop_items[x][i][stats[c]]
                            if stats[c] == "COST":
                                cost = shop_items[x][i][stats[c]]
                        name = i.title()
                        value = f"**Type:** {decs}"
                        embed.add_field(name=name, value=value, inline=False)
            await ctx.send(embed=embed)
        elif page == "2":
            embed = discord.Embed(title="Cat Merchant's Market: Lootboxes", color=ctx.author.color,
                                  description="Chests are filled with sussy suprises")
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/881990844226367531/882011191571017828/d6eo11s-c5758f3b-b486-4c49-9183-f56247fa7f7e.gif")
            embed.set_footer(
                text="page 2/4", icon_url="https://cdn.discordapp.com/attachments/881990844226367531/882013336726802453/a1ea1a79459efaa.png")
            shop_items = helper.shop_items
            for x in shop_items:
                if x == "Chests":
                    for i in shop_items[x]:
                        stats = list(shop_items[x][i].keys())
                        for c in range(len(stats)):
                            if stats[c] == "EMOJI":
                                emoji = shop_items[x][i][stats[c]]
                            if stats[c] == "DROPRATES":
                                rate = shop_items[x][i][stats[c]]
                            if stats[c] == "COST":
                                cost = shop_items[x][i][stats[c]]
                        name = i.title() + " " + emoji
                        value = f"**Cost:** {cost}\n**Droprates:** {rate}"
                        embed.add_field(name=name, value=value, inline=False)
            await ctx.send(embed=embed)
        elif page == "3":
            embed = discord.Embed(title="Cat Merchant's Market: Cat Potions", color=ctx.author.color,
                                  description="Potions will activate during the third round and can only activate once per battle.")
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/881990844226367531/882011191571017828/d6eo11s-c5758f3b-b486-4c49-9183-f56247fa7f7e.gif")
            embed.set_footer(
                text="page 3/4", icon_url="https://cdn.discordapp.com/attachments/881990844226367531/882013336726802453/a1ea1a79459efaa.png")
            shop_items = helper.shop_items
            for x in shop_items:
                if x == "Potions":
                    for i in shop_items[x]:
                        stats = list(shop_items[x][i].keys())
                        for c in range(len(stats)):
                            if stats[c] == "DESCRIPTION":
                                decs = shop_items[x][i][stats[c]]
                            if stats[c] == "COST":
                                cost = shop_items[x][i][stats[c]]
                        name = i.title()
                        value = f"**Cost:** {cost}\n**Description:** {decs}"
                        embed.add_field(name=name, value=value, inline=False)
            await ctx.send(embed=embed)
        elif page == "4":
            embed = discord.Embed(title="Cat Merchant's Market: Miscellaneous Items", color=ctx.author.color,
                                  description="need misc item description")
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/881990844226367531/882011191571017828/d6eo11s-c5758f3b-b486-4c49-9183-f56247fa7f7e.gif")
            embed.set_footer(
                text="page 4/4", icon_url="https://cdn.discordapp.com/attachments/881990844226367531/882013336726802453/a1ea1a79459efaa.png")
            shop_items = helper.shop_items
            for x in shop_items:
                if x == "Miscellaneous Items":
                    for i in shop_items[x]:
                        stats = list(shop_items[x][i].keys())
                        for c in range(len(stats)):
                            if stats[c] == "DESCRIPTION":
                                decs = shop_items[x][i][stats[c]]
                            if stats[c] == "COST":
                                cost = shop_items[x][i][stats[c]]
                        name = i.title()
                        value = f"**Cost:** {cost}\n**Description:** {decs}"
                        embed.add_field(name=name, value=value, inline=False)
            await ctx.send(embed=embed)

    @commands.command(aliases=["s", "item"])
    async def search(self, ctx, *, item):
        # turn item into lower case so it can be found in helper.py dictionary
        # get all items
        item1 = []
        item2 = []
        item3 = []
        item4 = []
        item5 = []
        if item == "list":
            embed = discord.Embed(title="List of all existing items")
            items = helper.items
            item_title = item.title()
            for x in items:
                classes = x
                if classes == "Common Item":
                    for i in items[x]:
                        emoji = emojiSearch.search(str(i))
                        index = emoji + f"{i.title()}"
                        item1.append(index)
                        value = f", ".join(str(y) for y in item1)
                    await ctx.send(f"**Common Items**\n{value}")
                elif classes == "Uncommon Item":
                    for i in items[x]:
                        emoji = emojiSearch.search(str(i))
                        index = emoji + f"{i.title()}"
                        item2.append(index)
                        value = f", ".join(str(y) for y in item2)
                    await ctx.send(f"**Uncommon Items**\n{value}")
                elif classes == "Rare Item":
                    for i in items[x]:
                        emoji = emojiSearch.search(str(i))
                        index = emoji + f"{i.title()}"
                        item3.append(index)
                        value = f", ".join(str(y) for y in item3)
                    await ctx.send(f"**Rare Items**\n{value}")
                elif classes == "Epic Item":
                    for i in items[x]:
                        emoji = emojiSearch.search(str(i))
                        index = emoji + f"{i.title()}"
                        item4.append(index)
                        value = f", ".join(str(y) for y in item4)
                    await ctx.send(f"**Epic Items**\n{value}")
                elif classes == "Legendary Item":
                    for i in items[x]:
                        emoji = emojiSearch.search(str(i))
                        index = emoji + f"{i.title()}"
                        item5.append(index)
                        value = f", ".join(str(y) for y in item5)
                    await ctx.send(f"**Legendary Items**\n{value}")


        else:
            item = item.lower()
            items = helper.items
            item_title = item.title()
            for x in items:
                # iterate through rarity (common, uncommon, rare, etc)
                rarity = x
                for i in items[x]:
                    # iterate through items inside of rarity
                    if i == item:
                        stats = list(items[x][i].keys())
                        for c in range(len(stats)):
                            # put description in embed description and not a field
                            if stats[c] == "DESCRIPTION":
                                description = items[x][i][stats[c]]
                            if stats[c] == "EMOJI":
                                emoji = items[x][i][stats[c]]
                            if stats[c] == "URL":
                                url = items[x][i][stats[c]]
                        description1 = description
                        item_title1 = rarity + ": " + item_title
                        embed = discord.Embed(
                            title=f"{item_title1}", description=description1, color=ctx.author.color)
                        embed.set_thumbnail(url=f"{url}")
                        for c in range(len(stats)):
                            # dumb way to do it but my brain is dying
                            if stats[c] != "EMOJI":
                                if stats[c] != "DESCRIPTION":
                                    if stats[c] != "URL":
                                        embed.add_field(
                                            name=stats[c], value=items[x][i][stats[c]], inline=False)
                        await ctx.send(embed=embed)



    @commands.command(aliases=['inv', 'pp6'])
    async def inventory(self, ctx, page = 1, member: discord.Member = None):
        if member == None:
            await helper.get_user(ctx.author.id, ctx)
            member = ctx.author
            author_stats = collection.find_one({"_id": member.id})
            


            embed = discord.Embed()
            embed.set_author(
                name=f"{ctx.author.name}'s Inventory", icon_url=ctx.author.avatar_url,)

            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/881990844226367531/882085132419338260/3W72119s5BjWPGGUiZ9pqnZoj8JHYxCCp9dtn2QVfABSuQxvBph92DDQwbqdijBQPGXRNtG68Qa5jLMMq6wWNV5TsKnw6gZfKy2P.png")

            # find total amount of pages(items / 6)

            totalPages = math.ceil(len(author_stats["Items"])/6)
            page = int(page)

            for i in range(page * 6 - 6, page * 6):
                try:
                    name = list(author_stats["Items"][i].keys())
                    names = name[0].title()

                    emoji = emojiSearch.search(names.lower())
                    if emoji != None:
                        names = name[0].title() + " " + emoji

                    embed.add_field(
                        name=names, value=author_stats["Items"][i][name[0]], inline=False)

                except Exception as e:
                    pass

            embed.set_footer(text="Page: " + str(page) + "/" + str(totalPages),
                             icon_url="https://cdn.discordapp.com/attachments/883009675006705734/883009716136079430/PngItem_45857_1.png")
            msg = await ctx.send(embed=embed)

            
        else:
            await helper.get_member(member, ctx)
            author_stats = collection.find_one({"_id": member.id})
            
            embed = discord.Embed()
            embed.set_author(
                name=f"{member.name}'s Inventory", icon_url=member.avatar_url)
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/881990844226367531/882085132419338260/3W72119s5BjWPGGUiZ9pqnZoj8JHYxCCp9dtn2QVfABSuQxvBph92DDQwbqdijBQPGXRNtG68Qa5jLMMq6wWNV5TsKnw6gZfKy2P.png")
            member = member
            
            
            # find total amount of pages(items / 6)

            totalPages = math.ceil(len(author_stats["Items"])/6)
            page = int(page)

            for i in range(page * 6 - 6, page * 6):
                try:
                    name = list(author_stats["Items"][i].keys())
                    names = name[0].title()

                    emoji = emojiSearch.search(names.lower())
                    if emoji != None:
                        names = name[0].title() + " " + emoji

                    embed.add_field(
                        name=names, value=author_stats["Items"][i][name[0]], inline=False)

                except Exception as e:
                    pass

            embed.set_footer(text="Page: " + str(page) + "/" + str(totalPages),
                             icon_url="https://cdn.discordapp.com/attachments/883009675006705734/883009716136079430/PngItem_45857_1.png")
            await ctx.send(embed=embed)

    @commands.command()
    async def unequip(self, ctx, *, item):
        # find item in equiped item list
        # delete it from the list using index
        item = item.lower()
        inventory = collection.find_one({"_id": ctx.author.id})
        unEquiped = False
        for i in range(len(inventory["EquipedItems"])):

            names = list(inventory["EquipedItems"][i].keys())
            print(names)
            if names[0] == item:
                print(inventory["EquipedItems"][i])
                inventory["EquipedItems"].pop(i)
                unEquiped = True
                await ctx.send("Unequiped item")
                itemStats = battleItemsSearch.search(item)

                for i in itemStats:

                    if i == "Health":
                        inventory['Cats'][0]['HP'] -= int(itemStats[i])
                    if i == "Attack":
                        inventory['Cats'][0]['ATK'] -= int(itemStats[i])
                    if i == "Defense":
                        inventory['Cats'][0]['DEF'] -= int(itemStats[i])

                    if i == "Speed":
                        inventory['Cats'][0]['SPD'] -= int(itemStats[i])



                post = inventory
                collection.find_one_and_replace({"_id": ctx.author.id}, post)
                return
        if not unEquiped:
            await ctx.send("Could not unequip")

    @commands.command(aliases = ['ei'])
    async def equippeditems(self, ctx):

        embed = discord.Embed(title="Equipped Items:")
        embed.set_author(
            name=f"{ctx.author.name}'s Equiped Items", icon_url=ctx.author.avatar_url)
        member = ctx.author
        author_stats = collection.find_one({"_id": member.id})


        for i in range(len(author_stats["EquipedItems"])):
            
            names = list(author_stats["EquipedItems"][i].keys())

            if author_stats["EquipedItems"][i][names[0]]["DESCRIPTION"] != " ":
                print(author_stats["EquipedItems"][i][names[0]]["DESCRIPTION"])
                embed.add_field(name=names[0].title(), value=author_stats["EquipedItems"][i][names[0]]["DESCRIPTION"])
            else:
                embed.add_field(name=names[0].title(),value="No description @marco")
        await ctx.send(embed=embed)

    @commands.command()
    async def equip(self, ctx, *, item):
        inventory = collection.find_one({"_id": ctx.author.id})
        # find the item they want to equip
        # check if already equipped
        # add the items stats to the cat
        # copy the item from the helper.battleItems to the equipped item list
        item = item.lower()
        modHP = 0
        modDEF = 0
        modATK = 0
        modSPD = 0
        found = False
        if len(inventory["EquipedItems"]) >= 6:
            await ctx.send("You cannot equip more items")
            return

        for x in range(len(inventory["EquipedItems"])):
            keys = list(inventory["EquipedItems"][x].keys())

            if keys[0] == item:
                await ctx.send("You already equipped this item")
                return

        for i in range(len(inventory["Items"])):

            print(inventory["Items"])
            names = list(inventory["Items"][i].keys())
            print(names)
            if len(names) > 0:
                name = names[0]
            else:
                name = None

            if name == item:
                itemStats = battleItemsSearch.search(item)
                found = True

                for i in itemStats:

                    if i == "Health" and inventory['Cats'][0]['HP'] + int(itemStats[i]) > 0:
                        inventory['Cats'][0]['HP'] += int(itemStats[i])
                        modHP += int(itemStats[i])

                    if i == "Attack" and inventory['Cats'][0]['ATK'] + int(itemStats[i]) > 0:
                        inventory['Cats'][0]['ATK'] += int(itemStats[i])
                        modATK += int(itemStats[i])

                    if i == "Defense" and inventory['Cats'][0]['DEF'] + int(itemStats[i]) > 0:
                        inventory['Cats'][0]['DEF'] += int(itemStats[i])
                        modDEF += int(itemStats[i])

                    if i == "Speed" and inventory['Cats'][0]['SPD'] + int(itemStats[i]) > 0:
                        inventory['Cats'][0]['SPD'] += int(itemStats[i])
                        modSPD += int(itemStats[i])



                inventory["EquipedItems"].append({name: itemStats})
                post = inventory
                collection.find_one_and_replace({"_id": ctx.author.id}, post)
        if not found:
            await ctx.send("Could not find item in your inventory")
        else:
            await ctx.send(f'Succesfully equiped {item}')


#commands to work on################

    @commands.command()
    async def gift(self, ctx, member: discord.Member, amount, *, item):
        try:
            amount = int(amount)
        except ValueError:
            await ctx.send("please specify amount to gift")
            return
        exist = await helper.get_member(member, ctx)
        if exist == None:
            return
        # check if item exist
        existingitem = emojiSearch.find_item_exists(item)
        if existingitem == None:
            await ctx.send(f"{ctx.author.mention} that item doesn't even exist")
            return
        await helper.get_user(ctx.author.id, ctx)
        # giving each other items
        if member == None:
            await ctx.send("Mention someone to give the item to")
            return
        # get user info
        author_stats = collection.find_one({"_id": ctx.author.id})
        member_stats = collection.find_one({"_id": member.id})
        amount = int(amount)
        hasItem = emojiSearch.check_has_item(item, author_stats)
        if hasItem == None:
            await ctx.send(f"{ctx.author.mention} you dont have {item} in your inventory")
            return
        elif hasItem != None:
            for i in range(len(author_stats["Items"])):
                has_item_amount = True
                try:
                    item_amount = author_stats["Items"][i][item]
                    if item_amount < amount:
                        await ctx.send(f"You don't have enough {item}s in your inventory")
                        return
                except Exception as e:
                    print(e)

                if item in author_stats["Items"][i]:
                    author_stats["Items"][i][item] -= amount

                    post = author_stats
                    collection.find_one_and_replace(
                        {"_id": ctx.author.id}, post)
                    if author_stats["Items"][i][item] == 0:

                        author_stats["Items"].pop(i)
                        post = author_stats
                        collection.find_one_and_replace(
                            {"_id": ctx.author.id}, post)

        member_has_item = emojiSearch.check_has_item(item, member_stats)
        if member_has_item != None:
            for i in range(len(member_stats["Items"])):
                if member_has_item in member_stats["Items"][i]:
                    member_stats["Items"][i][item] += amount
                    post = member_stats
                    collection.find_one_and_replace({"_id": member.id}, post)
                trade = True
        elif member_has_item == None:
            member_stats["Items"].append({item: amount})
            post = member_stats
            collection.find_one_and_replace({"_id": member.id}, post)

            trade = True
        if trade:
            await ctx.send(f"{ctx.author.mention} gave {amount} {item} to {member.mention}")

        else:
            await ctx.send("what the hell happened")

    @gift.error
    async def gift_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("please specify amount to gift")


##fix this up##


    @commands.command()
    async def sell(self, ctx, amount, *, item):
        author = collection.find_one({"_id": ctx.author.id})
        has_item = emojiSearch.check_has_item(item, author)
        check_item_exist = emojiSearch.find_item_exists(item)
        if check_item_exist == None:
            await ctx.send(f"that item doesn't exist <:Que:875459981170851950>")
            return
        if has_item == None:
            await ctx.send(f"{ctx.author.mention} you don't have {item} in your inventory")
            return
        else:
            pass
        try:
            amount = int(amount)
        except ValueError:
            await ctx.send("please specify amount to sell")
            return
        await helper.get_user(ctx.author.id, ctx)
        user_stats = collection.find_one({"_id": ctx.author.id})
        shop_items = helper.shop_items
        items = False
        for x in shop_items:
            # iterating through shop item category
            for i in shop_items[x]:
                if item == i:
                    items = True
                    amount = int(amount)
                    stats = list(shop_items[x][i].keys())
                    for c in range(len(stats)):
                        if stats[c] == "COST":
                            cost = shop_items[x][i][stats[c]]
                    sell_amount1 = cost * 0.6
                    sell_amount = round(sell_amount1)
                    sell = False
                    for i in range(len(user_stats["Items"])):
                        if item in user_stats["Items"][i]:
                            user_stats["Items"][i][item] -= amount
                            sell = True
                            if user_stats["Items"][i][item] == 0:
                                user_stats["Items"].pop(i)
                                post = user_stats
                                collection.find_one_and_replace(
                                    {"_id": ctx.author.id}, post)
                    if sell:
                        user_stats['Balance'] += sell_amount
                        await ctx.send(f"{ctx.author.mention} Successfully sold {amount} {item}, and got {sell_amount} gold.")
        if items == False:
            await ctx.send("item doesn't exist")
        else:
            post = user_stats
            collection.find_one_and_replace({'_id': ctx.author.id}, post)

    @sell.error
    async def sell_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("please specify amount to sell")

    @commands.command(aliases=['buy'])
    async def purchase(self, ctx, amount, *, item):
        try:
            amount = int(amount)
        except ValueError:
            await ctx.send("please specify amount to buy")
            return
        await helper.get_user(ctx.author.id, ctx)
        user_stats = collection.find_one({"_id": ctx.author.id})
        shop_items = helper.shop_items
        items = False
        for x in shop_items:
            # iterating through shop item category
            for i in shop_items[x]:
                if item == i:
                    items = True
                    amount = int(amount)
                    money = user_stats["Balance"]
                    # check if user has enough money for the item
                    stats = list(shop_items[x][i].keys())
                    bought = False
                    broke = False
                    for c in range(len(stats)):
                        if stats[c] == "COST":
                            # get the cost
                            cost = shop_items[x][i][stats[c]]
                    cost = amount * cost
                    if money < cost:
                        broke = True
                        await ctx.send(f"{ctx.author.mention} you don't have enough money in your balance to buy a `{item}`", delete_after=5)
                        break
                    hasItem = False
                    if not broke:
                        for i in range(len(user_stats["Items"])):
                            if item in user_stats["Items"][i]:
                                user_stats["Items"][i][item] += amount
                                hasItem = True
                            bought = True

                        if hasItem != True:
                            user_stats["Items"].append({item: amount})
                            bought = True

                    if bought:
                        user_stats["Balance"] -= cost
                        await ctx.send(f"{ctx.author.mention} Successfully bought {amount} {item}, costing you {cost}")
                    if broke:
                        await ctx.send(f"{ctx.author.mention} you don't have enough money in your balance to buy a `{item}`", delete_after=5)
        if items == False:
            await ctx.send("item doesn't exist")
        else:
            post = user_stats
            collection.find_one_and_replace({'_id': ctx.author.id}, post)

    @purchase.error
    async def purchase_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("please specify amount to buy")

    @commands.command(aliases = ['combine'])
    async def combiner(self, ctx, *items):
        authorInfo = collection.find_one({"_id": ctx.author.id})

        # combines items

        # check if tier of items are all the same
        # then check if they are all in the inventory
        # have to check if you have enough items
        # delete the items from the inventory
        # choose a random item from the tier above

        itemsRarity = []

        counter = Counter(items)

        if len(items) == 5:

            for i in range(len(items)):
                rarity = battleItemsSearch.searchRarity(items[i])
                print(items)
                if rarity != None:

                    if len(authorInfo["Items"]) >= len(counter):
                        for x in range(len(counter)):
                            for c in authorInfo["Items"][x]:
                                if authorInfo["Items"][x] == counter[x]:
                                    if authorInfo["Items"][x][c] - counter[items[i]] < 0:

                                        await ctx.send(f'You do not have enougth {items[x]}')
                                        return
                    if battleItemsSearch.check_equipped_boolean(items[i], authorInfo):
                        await ctx.send("One of your items is currently equipped")
                        return
                    if battleItemsSearch.check_has_item_boolean(items[i], authorInfo):
                        itemsRarity.append(rarity)

                    else:
                        print(items[i])
                        await ctx.send("You do not have one of the items")
                        return
                else:
                    await ctx.send(f'{items[i]} is not a valid item!')
                    return

            # checks if all the same rarity
            if itemsRarity.count(itemsRarity[0]) == len(itemsRarity):

                # deletes item
                toPop = []
                for item in items:
                    for i in range(len(authorInfo["Items"])):
                        print(i)
                        if item in authorInfo["Items"][i]:
                            authorInfo["Items"][i][item] -= 1

                            post = authorInfo
                            collection.find_one_and_replace(
                                {"_id": ctx.author.id}, post)
                            if authorInfo["Items"][i][item] == 0:
                                #####################################################TONY DO THIS PLEASE################################################
                                key = list(authorInfo["Items"][i].keys())

                                toPop.append(i)

                for i in sorted(toPop, reverse=True):
                    print(i)
                    print(authorInfo["Items"])
                    authorInfo["Items"].pop(i)
                    post = authorInfo
                    collection.find_one_and_replace(
                        {"_id": ctx.author.id}, post)

                # add random item from next rarity

                if rarity == "Common Item":
                    randomItem = random.choice(
                        list(helper.battleItems["Uncommon Item"].keys()))

                    if battleItemsSearch.check_has_item_boolean(randomItem, authorInfo):
                        index = battleItemsSearch.check_has_item_index(
                            random, authorInfo)
                        authorInfo["Items"][index][randomItem] += 1
                        post = authorInfo
                        collection.find_one_and_replace(
                            {"_id": ctx.author.id}, post)
                    else:
                        authorInfo["Items"].append({randomItem: 1})
                        post = authorInfo
                        collection.find_one_and_replace(
                            {"_id": ctx.author.id}, post)
                    await ctx.send(f'You got a {randomItem.title()}!')
                elif rarity == "Uncommon Item":
                    randomItem = random.choice(
                        list(helper.battleItems["Rare Item"].keys()))

                    if battleItemsSearch.check_has_item_boolean(randomItem, authorInfo):
                        index = battleItemsSearch.check_has_item_index(
                            random, authorInfo)
                        authorInfo["Items"][index][randomItem] += 1
                        post = authorInfo
                        collection.find_one_and_replace(
                            {"_id": ctx.author.id}, post)
                    else:
                        authorInfo["Items"].append({randomItem: 1})
                        post = authorInfo
                        collection.find_one_and_replace(
                            {"_id": ctx.author.id}, post)

                    await ctx.send(f'You got a {randomItem.title()}!')

            else:
                await ctx.send("Not all items are the same rarity")

        else:
            await ctx.send("You did not send enough items or too many items")

    @commands.command(aliases=['use'])
    async def opening(self, ctx, *, item):
        print(f"Opening chest{datetime.now().time()}")
        authorname = emojiSearch.get_user_name(self, ctx.author.id)
        authorInfo = collection.find_one({'_id':ctx.author.id})
        has_item = emojiSearch.check_has_item(item, authorInfo)
        item_exist = emojiSearch.find_item_exists(item)
        green_url = "https://cdn.discordapp.com/attachments/883009675006705734/885288993992871958/GreenChest.png"
        blue_url = "https://cdn.discordapp.com/attachments/883009675006705734/885288990121558076/BlueChest.png"
        purple_url = "https://cdn.discordapp.com/attachments/883009675006705734/885288996811452446/PurpleChest.png"
        red_url = "https://cdn.discordapp.com/attachments/883009675006705734/885289000062046298/RedChest.png",
        black_url = "https://cdn.discordapp.com/attachments/883009675006705734/885288985629454426/BlackChest.png"
        if not item_exist:
            await ctx.send(f"{ctx.author.mention} that item doesn't even exist")
            return
        elif not has_item:
            await ctx.send(f"{ctx.author.mention} you don't have {item} in your inventory")
            return

        green_chest = ['green', 'green chest', 'green box']
        print("759")


        ###READ THIS BRIAN###

        #1. DO NOT TOUCH ANY OF THIS CODE
        #2. DO NOT COPY AND PASTE THIS CODE UNLESS YOU **UNDERSTAND** IT
        #3. IF YOU DO NOT UNDERSTAND IT ASK ME
        #4. I WILL TRY MY BEST TO COMMENT WHAT IT DOES


        if item == "green chest":
            chance = random.randint(1, 100)
            print("761")
            if chance == 100:
                #1% chance 
                await emojiSearch.lootboxItems(ctx, authorInfo, "Legendary Item", authorname, item, green_url)
                return
            elif chance > 96:
                #100 - 3 = 96 because > does not include 96 so it starts at 97 so therefore 3%
                await emojiSearch.lootboxItems(ctx, authorInfo, "Epic Item", authorname, item, green_url)
                return
            elif chance > 90:
                #96 - 6 = 90 6% 
                await emojiSearch.lootboxItems(ctx, authorInfo, "Rare Item", authorname, item, green_url)
                return
            elif chance > 50:
                #90 - 40 = 50 %40
                await emojiSearch.lootboxItems(ctx, authorInfo, "Uncommon Item", authorname, item, green_url)
                return
            elif chance > 0:
                #50 - 50 = 0 %50
                await emojiSearch.lootboxItems(ctx, authorInfo, "Common Item", authorname, item, green_url)
                return
        elif item == "blue chest":
            chance = random.randint(1, 100)
            if chance > 98:
                await emojiSearch.lootboxItems(ctx, authorInfo, "Legendary Item", authorname, item, blue_url)
                return
            elif chance > 92:
                await emojiSearch.lootboxItems(ctx, authorInfo, "Epic Item", authorname, item, blue_url)
                return
            
            elif chance > 70:
                await emojiSearch.lootboxItems(ctx, authorInfo, "Rare Item", authorname, item, blue_url)
                return
            
            elif chance > 40:
                await emojiSearch.lootboxItems(ctx, authorInfo, "Uncommon Item", authorname, item, blue_url)
                return
            elif chance > 0:
                await emojiSearch.lootboxItems(ctx, authorInfo, "Common Item", authorname, item, blue_url)
                return
        elif item == "purple chest":
            chance = random.randint(1, 100)
            if chance > 96:
                await emojiSearch.lootboxItems(ctx, authorInfo, "Legendary Item", authorname, item, blue_url)
                return
            elif chance > 81:
                await emojiSearch.lootboxItems(ctx, authorInfo, "Epic Item", authorname, item, blue_url)
                return
            
            elif chance > 46:
                await emojiSearch.lootboxItems(ctx, authorInfo, "Rare Item", authorname, item, blue_url)
                return
            
            elif chance > 20:
                await emojiSearch.lootboxItems(ctx, authorInfo, "Uncommon Item", authorname, item, blue_url)
                return
            elif chance > 0:
                await emojiSearch.lootboxItems(ctx, authorInfo, "Common Item", authorname, item, blue_url)
                return
        elif item == "red chest":
            chance = random.randint(1, 100)
            if chance > 90:
                await emojiSearch.lootboxItems(ctx, authorInfo, "Legendary Item", authorname, item, blue_url)
                return
            elif chance > 60:
                await emojiSearch.lootboxItems(ctx, authorInfo, "Epic Item", authorname, item, blue_url)
                return
            
            elif chance > 30:
                await emojiSearch.lootboxItems(ctx, authorInfo, "Rare Item", authorname, item, blue_url)
                return
            
            elif chance > 15:
                await emojiSearch.lootboxItems(ctx, authorInfo, "Uncommon Item", authorname, item, blue_url)
                return
            elif chance > 0:
                await emojiSearch.lootboxItems(ctx, authorInfo, "Common Item", authorname, item, blue_url)
                return
        elif item == "black chest":
            chance = random.randint(1, 100)
            if chance < 50:
                await emojiSearch.lootboxItems(ctx, authorInfo, "Epic Item", authorname, item, black_url)
                return
            elif chance > 50:
                await emojiSearch.lootboxItems(ctx, authorInfo, "Legendary Item", authorname, item, black_url)
                return
        
        index = battleItemsSearch.check_has_item_index(item, authorInfo)
        if authorInfo["Items"][index][item] > 1:
            authorInfo["Items"][index][item] -= 1
            post = authorInfo
            collection.find_one_and_replace({"_id": ctx.author.id}, post)
        else:
            authorInfo["Items"].pop(index)
            post = authorInfo
            collection.find_one_and_replace({"_id": ctx.author.id}, post)
    





    @commands.command()
    async def trader(self, ctx):
        # combining traits
        pass


def setup(bot):
    bot.add_cog(Items(bot))
