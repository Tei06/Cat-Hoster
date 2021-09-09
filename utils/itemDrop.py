import random
from utils import battleItemsSearch
from utils import helper
import pymongo
import discord


mongo_url = "mongodb+srv://Tei:yeet123LMAO@shizukudb.rt4ys.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
cluster = pymongo.MongoClient(mongo_url)
db = cluster["ShizukuDB"]
collection = db['new']

async def itemDrop(self, ctx, rarity):
        #drops a random item depending on rarity

        #find rarity of cat
        #choose random item depending on drop rates


        authorInfo = collection.find_one({"_id": ctx.author.id})

        chance = random.randint(0, 100)

        if rarity == "Common":
            if chance == 100:
                randomItem = random.choice(list(helper.battleItems["Uncommon Item"].keys()))
                if battleItemsSearch.check_has_item_boolean(randomItem, authorInfo):
                    index = battleItemsSearch.check_has_item_index(randomItem, authorInfo)
                    authorInfo["Items"][index][randomItem] += 1
                    post = authorInfo
                    collection.find_one_and_replace({"_id": ctx.author.id}, post)
                else:
                    authorInfo["Items"].append({randomItem: 1})
                    post = authorInfo
                    collection.find_one_and_replace({"_id": ctx.author.id}, post)
                await ctx.send(f'You got a {randomItem.title()}!')
            elif chance > 95:
                randomItem = random.choice(list(helper.battleItems["Common Item"].keys()))
                if battleItemsSearch.check_has_item_boolean(randomItem, authorInfo):
                    index = battleItemsSearch.check_has_item_index(randomItem, authorInfo)
                    authorInfo["Items"][index][randomItem] += 1
                    post = authorInfo
                    collection.find_one_and_replace({"_id": ctx.author.id}, post)
                else:
                    authorInfo["Items"].append({randomItem: 1})
                    post = authorInfo
                    collection.find_one_and_replace({"_id": ctx.author.id}, post)
                await ctx.send(f'You got a {randomItem.title()}!')


        #uncommon cat
        elif rarity == "Uncommon":
            if chance > 96:
                randomItem = random.choice(list(helper.battleItems["Uncommon Item"].keys()))
                if battleItemsSearch.check_has_item_boolean(randomItem, authorInfo):
                    index = battleItemsSearch.check_has_item_index(randomItem, authorInfo)
                    authorInfo["Items"][index][randomItem] += 1
                    post = authorInfo
                    collection.find_one_and_replace({"_id": ctx.author.id}, post)
                else:
                    authorInfo["Items"].append({randomItem: 1})
                    post = authorInfo
                    collection.find_one_and_replace({"_id": ctx.author.id}, post)
                await ctx.send(f'You got a {randomItem.title()}!')
            elif chance > 90:
                randomItem = random.choice(list(helper.battleItems["Common Item"].keys()))
                if battleItemsSearch.check_has_item_boolean(randomItem, authorInfo):
                    index = battleItemsSearch.check_has_item_index(randomItem, authorInfo)
                    authorInfo["Items"][index][randomItem] += 1
                    post = authorInfo
                    collection.find_one_and_replace({"_id": ctx.author.id}, post)
                else:
                    authorInfo["Items"].append({randomItem: 1})
                    post = authorInfo
                    collection.find_one_and_replace({"_id": ctx.author.id}, post)
                await ctx.send(f'You got a {randomItem.title()}!')


        #rare cat
        elif rarity == "Rare":
            if chance > 98:
                randomItem = random.choice(list(helper.battleItems["Rare Item"].keys()))
                if battleItemsSearch.check_has_item_boolean(randomItem, authorInfo):
                    index = battleItemsSearch.check_has_item_index(randomItem, authorInfo)
                    authorInfo["Items"][index][randomItem] += 1
                    post = authorInfo
                    collection.find_one_and_replace({"_id": ctx.author.id}, post)
                else:
                    authorInfo["Items"].append({randomItem: 1})
                    post = authorInfo
                    collection.find_one_and_replace({"_id": ctx.author.id}, post)
                await ctx.send(f'You got a {randomItem.title()}!')
            elif chance > 92:
                randomItem = random.choice(list(helper.battleItems["Uncommon Item"].keys()))
                if battleItemsSearch.check_has_item_boolean(randomItem, authorInfo):
                    index = battleItemsSearch.check_has_item_index(randomItem, authorInfo)
                    authorInfo["Items"][index][randomItem] += 1
                    post = authorInfo
                    collection.find_one_and_replace({"_id": ctx.author.id}, post)
                else:
                    authorInfo["Items"].append({randomItem: 1})
                    post = authorInfo
                    collection.find_one_and_replace({"_id": ctx.author.id}, post)
                await ctx.send(f'You got a {randomItem.title()}!')
            elif chance > 80:
                randomItem = random.choice(list(helper.battleItems["Common Item"].keys()))
                if battleItemsSearch.check_has_item_boolean(randomItem, authorInfo):
                    index = battleItemsSearch.check_has_item_index(randomItem, authorInfo)
                    authorInfo["Items"][index][randomItem] += 1
                    post = authorInfo
                    collection.find_one_and_replace({"_id": ctx.author.id}, post)
                else:
                    authorInfo["Items"].append({randomItem: 1})
                    post = authorInfo
                    collection.find_one_and_replace({"_id": ctx.author.id}, post)
                await ctx.send(f'You got a {randomItem.title()}!')
        

        #epic

        elif rarity == "Epic":
            #uncomment when epic items are added
            if chance > 96:
                randomItem = random.choice(list(helper.battleItems["Epic Item"].keys()))
                if battleItemsSearch.check_has_item_boolean(randomItem, authorInfo):
                    index = battleItemsSearch.check_has_item_index(randomItem, authorInfo)
                    authorInfo["Items"][index][randomItem] += 1
                    post = authorInfo
                    collection.find_one_and_replace({"_id": ctx.author.id}, post)
                else:
                    authorInfo["Items"].append({randomItem: 1})
                    post = authorInfo
                    collection.find_one_and_replace({"_id": ctx.author.id}, post)
                await ctx.send(f'You got a {randomItem.title()}!')
            elif chance > 90:
                randomItem = random.choice(list(helper.battleItems["Rare Item"].keys()))
                if battleItemsSearch.check_has_item_boolean(randomItem, authorInfo):
                    index = battleItemsSearch.check_has_item_index(randomItem, authorInfo)
                    authorInfo["Items"][index][randomItem] += 1
                    post = authorInfo
                    collection.find_one_and_replace({"_id": ctx.author.id}, post)
                else:
                    authorInfo["Items"].append({randomItem: 1})
                    post = authorInfo
                    collection.find_one_and_replace({"_id": ctx.author.id}, post)
                await ctx.send(f'You got a {randomItem.title()}!')
            elif chance > 80:
                randomItem = random.choice(list(helper.battleItems["Uncommon Item"].keys()))
                if battleItemsSearch.check_has_item_boolean(randomItem, authorInfo):
                    index = battleItemsSearch.check_has_item_index(randomItem, authorInfo)
                    authorInfo["Items"][index][randomItem] += 1
                    post = authorInfo
                    collection.find_one_and_replace({"_id": ctx.author.id}, post)
                else:
                    authorInfo["Items"].append({randomItem: 1})
                    post = authorInfo
                    collection.find_one_and_replace({"_id": ctx.author.id}, post)
                await ctx.send(f'You got a {randomItem.title()}!')
            elif chance > 60:
                randomItem = random.choice(list(helper.battleItems["Common Item"].keys()))
                if battleItemsSearch.check_has_item_boolean(randomItem, authorInfo):
                    index = battleItemsSearch.check_has_item_index(randomItem, authorInfo)
                    authorInfo["Items"][index][randomItem] += 1
                    post = authorInfo
                    collection.find_one_and_replace({"_id": ctx.author.id}, post)
                else:
                    authorInfo["Items"].append({randomItem: 1})
                    post = authorInfo
                    collection.find_one_and_replace({"_id": ctx.author.id}, post)
                await ctx.send(f'You got a {randomItem.title()}!')
        

        #legendary
        elif rarity == "Legendary":
            #uncomment when added
            if chance > 95:
                randomItem = random.choice(list(helper.battleItems["Legendary Item"].keys()))
                if battleItemsSearch.check_has_item_boolean(randomItem, authorInfo):
                    index = battleItemsSearch.check_has_item_index(randomItem, authorInfo)
                    authorInfo["Items"][index][randomItem] += 1
                    post = authorInfo
                    collection.find_one_and_replace({"_id": ctx.author.id}, post)
                else:
                    authorInfo["Items"].append({randomItem: 1})
                    post = authorInfo
                    collection.find_one_and_replace({"_id": ctx.author.id}, post)
                await ctx.send(f'You got a {randomItem.title()}!')
            
            elif chance > 85:
                randomItem = random.choice(list(helper.battleItems["Epic Item"].keys()))
                if battleItemsSearch.check_has_item_boolean(randomItem, authorInfo):
                    index = battleItemsSearch.check_has_item_index(randomItem, authorInfo)
                    authorInfo["Items"][index][randomItem] += 1
                    post = authorInfo
                    collection.find_one_and_replace({"_id": ctx.author.id}, post)
                else:
                    authorInfo["Items"].append({randomItem: 1})
                    post = authorInfo
                    collection.find_one_and_replace({"_id": ctx.author.id}, post)
                await ctx.send(f'You got a {randomItem.title()}!')
            if chance > 75:
                randomItem = random.choice(list(helper.battleItems["Rare Item"].keys()))
                if battleItemsSearch.check_has_item_boolean(randomItem, authorInfo):
                    index = battleItemsSearch.check_has_item_index(randomItem, authorInfo)
                    authorInfo["Items"][index][randomItem] += 1
                    post = authorInfo
                    collection.find_one_and_replace({"_id": ctx.author.id}, post)
                else:
                    authorInfo["Items"].append({randomItem: 1})
                    post = authorInfo
                    collection.find_one_and_replace({"_id": ctx.author.id}, post)
                await ctx.send(f'You got a {randomItem.title()}!')
            elif chance > 65:
                randomItem = random.choice(list(helper.battleItems["Uncommon Item"].keys()))
                if battleItemsSearch.check_has_item_boolean(randomItem, authorInfo):
                    index = battleItemsSearch.check_has_item_index(randomItem, authorInfo)
                    authorInfo["Items"][index][randomItem] += 1
                    post = authorInfo
                    collection.find_one_and_replace({"_id": ctx.author.id}, post)
                else:
                    authorInfo["Items"].append({randomItem: 1})
                    post = authorInfo
                    collection.find_one_and_replace({"_id": ctx.author.id}, post)
                await ctx.send(f'You got a {randomItem.title()}!')
            elif chance > 50:
                randomItem = random.choice(list(helper.battleItems["Common Item"].keys()))
                if battleItemsSearch.check_has_item_boolean(randomItem, authorInfo):
                    index = battleItemsSearch.check_has_item_index(randomItem, authorInfo)
                    authorInfo["Items"][index][randomItem] += 1
                    post = authorInfo
                    collection.find_one_and_replace({"_id": ctx.author.id}, post)
                else:
                    authorInfo["Items"].append({randomItem: 1})
                    post = authorInfo
                    collection.find_one_and_replace({"_id": ctx.author.id}, post)
                await ctx.send(f'You got a {randomItem.title()}!')