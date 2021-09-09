import pymongo
import discord
from discord.ext import commands
import random
import asyncio
from cogs import catexp 
from utils import emojiSearch, itemDrop, helper, battleItemsSearch

#mongo dbs
mongo_urls = "mongodb+srv://brian:brianisawesome@cluster0.2tora.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
clusters = pymongo.MongoClient(mongo_urls)
dbs = clusters['ShizukuVouches']
col = dbs['Vouches']

mongo_url = "mongodb+srv://Tei:yeet123LMAO@shizukudb.rt4ys.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
cluster = pymongo.MongoClient(mongo_url)
db = cluster["ShizukuDB"]
collection = db['new']




class RevampedPve(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    def createPVEmbed(self, ctx, enemy, own, enemyHP, enemyStartingHP, ownStartingHP, rounds, round_number = None):
        #finds the percentage of filled in boxes
        if round_number == None:
            round_number = 1
        author_name = emojiSearch.get_user_name1(self, ctx.author.id)
        author_stats = collection.find_one({'_id':ctx.author.id})
        enemy_stats = col.find_one({'_id':ctx.author.id})
        equipped_item_emoji = ""
        if author_stats['EquipedItems'] == None:
            pass
        else:
            desc = []

            for i in range(len(author_stats["EquipedItems"])):
                names = list(author_stats["EquipedItems"][i].keys())
                emoji = emojiSearch.search(names[0])
                desc.append(emoji)
            equipped_item_emoji = " ".join(desc)
        enemy_equipped_item_emoji = ""
        if enemy_stats['enemyCat']['enemyCatEquippedItem'] == None:
            pass
        else:
            desc2 = []
            
            emojis = emojiSearch.search(enemy_stats['enemyCat']['enemyCatEquippedItem'])
            desc2.append(emojis)
            enemy_equipped_item_emoji = " ".join(desc2)
    
        
        try:
            if enemyHP >= 0:
                enemyPercentage = enemyHP/enemyStartingHP
            else:
                enemyPercentage = 0
        except:
            enemyPercentage = 0
        enemyBoxes = int(15*enemyPercentage)
        try:
            ourPercentage = own['Cats'][0]['HP']/ownStartingHP
        except:
            ourPercentage = 0
        boxes = int(15*ourPercentage)
        hp_emoji = "<:purpleheart:884632967958376468>"

        enemy_level = enemy['enemyCat']['enemyCatLevel']
        enemy_hp = enemyHP
        rarity = enemy['enemyCat']['enemyCatRarity']
        enemy_hp_bar = enemyBoxes * ":red_square:" + (15-enemyBoxes) * ":white_large_square:"

        author_hp_bar = boxes * "<:hpfull:882088120823201862>" + (15-boxes) * "<a:hpempty:882082827057917984>"
        author_level = own['Cats'][0]['Level']
        author_hp = own['Cats'][0]['HP']
        author_cat_name = own["Cats"][0]["Name"]

        author_desc = f"__{author_name}'s__ Level {author_level} **{author_cat_name}**\n{equipped_item_emoji} \n **{author_hp}/{ownStartingHP}** {hp_emoji} \n{author_hp_bar}"
        enemy_desc = f"Enemy's **{rarity}** Level {enemy_level} Cat\n{enemy_equipped_item_emoji} \n **{enemy_hp}/{enemyStartingHP}** {hp_emoji}\n{enemy_hp_bar}"
        description = author_desc + "\n\n" + enemy_desc + "\n\n\n" + f"[Round {round_number}]" + "\n" + rounds
        embed = discord.Embed(description=description, colour=discord.Colour(0xff3600))
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/884966282942881812/884966300508647524/Daco_3555790.png")

        return embed

    
    def aiAttackCalc(self, ctx, ai, own, ownStartingHP):
        try:
            ourPercentage = own['Cats'][0]['HP']/ownStartingHP
        except:
            ourPercentage = 0
        ownPercent = (ourPercentage*100)
        
        if ownPercent <= 50:
            defense = round(random.uniform(0.65, 0.75), 2) #negating 25-35% incoming damage randomly if hp below 50
        else:
            defense = round(random.uniform(0.35, 0.50), 2) #negating 50-65% incoming damage randomly
        damageDealt = 0
        evasion = own['Cats'][0]['SPD'] / 5
        if evasion > 75:
            evasion = 75
        evasion_chance = random.randint(0, 100)

        missed = False
        damageDealt = 0
        crit = False
        fullGuard = False

        if evasion_chance < evasion:
            
            missed = True

        
            
        #bandaid for shitty code
        #holy shit this requirs a fucking rewrite
        
        if not missed:
            enemyATK = ai['enemyCat']['enemyCatAtk']
            crit_chance = random.randint(1, 100)
            crit_rate = 13
            rate = [0.3, 0.4, 0.5]
            crit_multiplier = random.choice(rate)
            if crit_chance <= crit_rate:
                damageDealt = own['Cats'][0]['HP'] - (own['Cats'][0]['HP'] - round((ai['enemyCat']['enemyCatAtk'] + ai['enemyCat']['enemyCatAtk'] * crit_multiplier) * defense))
                own['Cats'][0]['HP'] = own['Cats'][0]['HP'] - round((ai['enemyCat']['enemyCatAtk'] + ai['enemyCat']['enemyCatAtk'] * crit_multiplier) * defense)
                crit = True

            #more duct tape and bandaids!   
            if not crit:
                full_guard = own['Cats'][0]['DEF'] / 10 # every 10 defense has 1% chance of activating full guard
                chance = random.randint(1, 100)
                if full_guard >= chance:
                    full_defense = 0.1
                    damageDealt1 = own['Cats'][0]['HP'] - (own['Cats'][0]['HP'] - (round(enemyATK * full_defense)))
                    damageDealt = round(damageDealt1)
                    own['Cats'][0]['HP'] = own['Cats'][0]['HP'] - (round(enemyATK * full_defense))
                    fullGuard = True
                
                if not fullGuard:
                    #normal attack 
                    #enemies turn  
                    
                    #checks if enemy atk is under 75% of our def

                    damageDealt1 = own['Cats'][0]['HP'] - (own['Cats'][0]['HP'] - (round(enemyATK * defense)))
                    damageDealt = round(damageDealt1)
                    own['Cats'][0]['HP'] = own['Cats'][0]['HP'] - (round(enemyATK * defense))


        own['Cats'][0]['HP'] = int(own['Cats'][0]['HP'])

        return own, missed, crit, fullGuard, damageDealt


    def ownAttackCalc(self, ctx, ai, own, enemyHP, enemyStartingHP):
        try:
            if enemyHP >= 0:
                enemyPercentage = enemyHP/enemyStartingHP #enemyPercentage is a float
            else:
                enemyPercentage = 0
        except:
            enemyPercentage = 0

        enemyPercent = (enemyPercentage*100)
        if enemyPercent <= 50:
            defense = round(random.uniform(0.65, 0.75), 2) #negating 25-45% incoming damage randomly
        else:
            defense = round(random.uniform(0.35, 0.50), 2) #negating 35-45% incoming damage randomly
        
        missed = False
        damageDealt = 0
        crit = False
        fullGuard = False

        #evasion calculation
        evasion = ai['enemyCat']['enemyCatSpd'] / 5
        if evasion > 60:
            evasion = 60

        chance = random.randint(0, 100)
        damageDealt = 0
        
        if chance < evasion:   # health - incoming damage that is negated by defense
            
            missed = True
        if not missed:
            crit_chance = random.randint(1, 100)
            crit_rate = 20
            rate = [0.4, 0.5]
            crit_multiplier = random.choice(rate)
            if crit_chance <= crit_rate:
                damageDealt1 = round(ai['enemyCat']['enemyCatHP'] - (ai['enemyCat']['enemyCatHP'] - round((own['Cats'][0]['ATK'] + own['Cats'][0]['ATK'] * crit_multiplier)*defense)))
                damageDealt = round(damageDealt1)
                ai['enemyCat']['enemyCatHP'] = ai['enemyCat']['enemyCatHP'] - round((own['Cats'][0]['ATK'] + own['Cats'][0]['ATK'] * crit_multiplier)*defense)
                crit = True

            #could've just use a else but touching this code makes my brain die
            if not crit:
                full_guard = ai['enemyCat']['enemyCatDef'] / 10 # every 10 defense has 1% chance of activating full guard
                chance = random.randint(1, 100)
                if full_guard >= chance:
                    full_defense = 0.1
                    damageDealt = ai['enemyCat']['enemyCatHP'] - (ai['enemyCat']['enemyCatHP'] - (round(own['Cats'][0]['ATK'] * full_defense)))
                    ai['enemyCat']['enemyCatHP'] = ai['enemyCat']['enemyCatHP'] - (round(own['Cats'][0]['ATK'] * full_defense))
                    fullGuard = True

                #missed crit and full guard
                if not fullGuard:
                    damageDealt = ai['enemyCat']['enemyCatHP'] - (ai['enemyCat']['enemyCatHP'] - (round(own['Cats'][0]['ATK'] * defense)))
                    ai['enemyCat']['enemyCatHP'] = ai['enemyCat']['enemyCatHP'] - (round(own['Cats'][0]['ATK'] * defense))


        ai['enemyCat']['enemyCatHP'] = int(ai['enemyCat']['enemyCatHP'])



        return ai, missed, crit, fullGuard, damageDealt

    async def attack(self, ctx, startingHP, msg, enemyStartingHP):
        #enemy db
        enemy = col.find_one({'_id': ctx.author.id})
        own = collection.find_one({'_id': ctx.author.id})
        author_cat_name = own["Cats"][0]['Name']
        rounds = 1

        
        if enemy != None:
            while True:
                miss = [f"**{author_cat_name}** tripped over a rock a missed their attack", 
                f"**{author_cat_name}** stubbed their toe and missed their attack", 
                f"**{author_cat_name}** got distracted by a butterfly and missed their attack"]
                missing = random.choice(miss)
                rounds += 1
                enemy, missed, crit, fullGuard, damageDealt = self.ownAttackCalc(ctx, enemy, own, enemy['enemyCat']['enemyCatHP'], enemyStartingHP)
                if missed:
                    embed = self.createPVEmbed(ctx, enemy, own, enemy['enemyCat']['enemyCatHP'], enemyStartingHP, startingHP, f"{missing}", rounds)
                elif crit:
                    embed = self.createPVEmbed(ctx, enemy, own, enemy['enemyCat']['enemyCatHP'], enemyStartingHP, startingHP, f"__{author_cat_name}__ cat dealt **{damageDealt} critical damage <:CriticalStrike:884812949343043694>**", rounds)
                elif fullGuard:
                    embed = self.createPVEmbed(ctx, enemy, own, enemy['enemyCat']['enemyCatHP'], enemyStartingHP, startingHP, f"__Enemy cat__ has **put up their gaurd!** {author_cat_name} only dealt {damageDealt} damage...", rounds)
                else:
                    embed = self.createPVEmbed(ctx, enemy, own, enemy['enemyCat']['enemyCatHP'], enemyStartingHP, startingHP, f"__{author_cat_name}__ cat dealt **{damageDealt} damage**", rounds)
                

                await msg.edit(embed=embed)

                await asyncio.sleep(2)

                #enemy died 
                if enemy['enemyCat']['enemyCatHP'] <= 0:
                    #add exp here
                    
                    await ctx.send("You Won!")
                    col.delete_one({'_id':ctx.author.id})
                    own['Cats'][0]['HP'] = startingHP
                    post = own
                    collection.replace_one({'_id':ctx.author.id}, post)
                    await catexp.CatExp.add_xp(ctx, ctx, enemy['enemyCat']['enemyCatRarity'])
                    await itemDrop.itemDrop(self, ctx, enemy['enemyCat']['enemyCatRarity'])
                    break
                #did not die, now its their turn!
                else:
                    post = enemy
                    stat = collection.find_one({'_id':ctx.author.id})
                    ownStartingHP = stat['Cats'][0]['HP']
                    post['enemyCat']['enemyCatHP'] = enemy['enemyCat']['enemyCatHP']
                    col.replace_one({'_id':ctx.author.id}, post)
                    rounds += 1
                    miss = [f"**{author_cat_name}** tripped over a rock a missed their attack", f"**{author_cat_name}** stubbed their toe and missed their attack", f"**{author_cat_name}** got distracted by a butterfly and missed their attack"]
                    missing = random.choice(miss)
                    own, missed, crit, fullGuard, damageDealt = self.aiAttackCalc(ctx, enemy, own, ownStartingHP)

                    if missed:
                        embed = self.createPVEmbed(ctx, enemy, own, enemy['enemyCat']['enemyCatHP'], enemyStartingHP, startingHP, f"{missing}", rounds)
                    elif crit:
                        embed = self.createPVEmbed(ctx, enemy, own, enemy['enemyCat']['enemyCatHP'], enemyStartingHP, startingHP, f"__Enemy cat__ has dealt **{damageDealt} critical damage <:CriticalStrike:884812949343043694>**", rounds)
                    elif fullGuard:
                        embed = self.createPVEmbed(ctx, enemy, own, enemy['enemyCat']['enemyCatHP'], enemyStartingHP, startingHP, f"__{author_cat_name}__ has **put up their gaurd!** Enemy cat only dealt {damageDealt} damage...", rounds)
                    else:
                        embed = self.createPVEmbed(ctx, enemy, own, enemy['enemyCat']['enemyCatHP'], enemyStartingHP, startingHP, f"__Enemy cat__ has dealt **{damageDealt} damage**", rounds)

                    await msg.edit(embed=embed)

                    post = own
                    collection.replace_one({'_id':ctx.author.id}, post)
                    

                    #we lost
                    if own['Cats'][0]['HP'] <= 0:
                        #add exp here
                        
                        await ctx.send("You Lost!")
                        col.delete_one({'_id':ctx.author.id})
                        own['Cats'][0]['HP'] = startingHP
                        post = own
                        collection.replace_one({'_id':ctx.author.id}, post)
                        await catexp.CatExp.add_xp(ctx, ctx, enemy['enemyCat']['enemyCatRarity'])
                        break


                    await asyncio.sleep(2)
        else:
            await ctx.send("You are not in a battle.")

    @commands.command(aliases = ['h'], brief="Fights a cat")
    async def hunt(self, ctx):
        stat = collection.find_one({'_id': ctx.author.id})
        enemy = col.find_one({"_id": ctx.author.id})
        if stat == None:
            await ctx.send(f"{ctx.author.mention} Please make an account first by doing `+start`", delete_after=10)
        elif enemy != None:
            await ctx.send(f"{ctx.author.mention} You are already in a battle", delete_after=10)
        else:
            #spawns a random cat
            startingHP = stat['Cats'][0]['HP']
        
            playerCatLevel = stat['Cats'][0]['Level']
            if playerCatLevel != 1:
                enemyCatLevel = playerCatLevel - 1
            else:
                enemyCatLevel = 1
            enemyCatHP = 100
            enemyCatDef = 20
            enemyCatAtk = 20
            enemyCatSpd = 20

            equipedItem = None

            if random.random() < 0.5:
                #adjust values later on
                if random.random() < 0.1:
                    equipedItem = random.choice(list(helper.battleItems["Rare Item"].keys()))
                elif random.random() < 0.5:
                    equipedItem = random.choice(list(helper.battleItems["Uncommon Item"].keys()))
                else:
                    equipedItem = random.choice(list(helper.battleItems["Common Item"].keys()))


                itemStats = battleItemsSearch.search(equipedItem)
                
                for i in itemStats:
                    if i == "Health":
                        enemyCatHP += int(itemStats[i])
                    if i == "Attack":
                        enemyCatAtk += int(itemStats[i])

                    if i == "Defense":
                        enemyCatDef += int(itemStats[i])

                    if i == "Speed":
                        enemyCatSpd += int(itemStats[i])

                await ctx.send(f'Enemy has a {equipedItem}')


            for i in range(enemyCatLevel - 1):
                enemyCatHP += 5
                statBoost = random.randint(0, 3)
                if statBoost == 0:
                    enemyCatHP += 25
                elif statBoost == 1:
                    enemyCatDef += 5
                elif statBoost == 2:
                    enemyCatAtk += 10
                elif statBoost == 3:
                    enemyCatSpd += 5

        
            rng = random.randint(0, 100)
            if rng > 95:
                enemyCatRarity = "Legendary"
            elif rng > 85:
                enemyCatRarity = "Epic"
            elif rng > 70:
                enemyCatRarity = "Rare"
            elif rng > 50:
                enemyCatRarity = "Uncommon"
            else:
                enemyCatRarity = "Common"
            #debug for testing drops
            enemyCatRarity = "Legendary"
            enemyCat = {
                'enemyName': "Cat",
                'enemyCatLevel': enemyCatLevel,
                'enemyCatHP': enemyCatHP,
                'enemyCatDef': enemyCatDef,
                'enemyCatAtk': enemyCatAtk,
                'enemyCatSpd': enemyCatSpd,
                'enemyCatRarity': enemyCatRarity,
                'enemyCatEquippedItem': equipedItem
            }
            post = {
                '_id': ctx.author.id,
                'enemyCat': enemyCat
            }
            col.insert_one(post)
            #embed and stuff
            stat = collection.find_one({'_id': ctx.author.id})
            enemy = col.find_one({"_id": ctx.author.id})
            ownSpeed = stat['Cats'][0]['SPD']
            enemySpeed = enemy['enemyCat']['enemyCatSpd']
            cat_name = stat['Cats'][0]['Name']

            

            if ownSpeed > enemySpeed:
                statement = f"__{cat_name}__ has **faster speed!** They make the first move <a:pandafight:875462064070623322>"
            elif enemySpeed > ownSpeed:
                statement = f"__Enemy cat__ has **faster speed!** They make the first move <a:pandafight:875462064070623322>"
            else:
                statement= f"Both cats have the **same speed!**\nA random cat will be chosen to make the first move <a:catwiggle:881368287332691999>"
            embed = self.createPVEmbed(ctx, post, stat, enemyCatHP, enemyCatHP, startingHP, statement)

            msg = await ctx.send(embed=embed)
            
            await asyncio.sleep(2)

            enemy = col.find_one({'_id': ctx.author.id})

            if stat['Cats'][0]['SPD'] < enemyCatSpd:
                own = collection.find_one({'_id':ctx.author.id})
                author_cat_name = own["Cats"][0]['Name']
                ownStartingHP = own['Cats'][0]['HP']
                miss = [f"The enemy cat tripped over a rock a missed their attack", f"The enemy cat stubbed their toe and missed their attack", f"The enemy cat got distracted by a butterfly and missed their attack"]
                missing = random.choice(miss)
                stat, missed, crit, fullGuard, damageDealt = self.aiAttackCalc(ctx, enemy, stat, ownStartingHP)
                if missed:
                    embed = self.createPVEmbed(ctx, enemy, stat, enemy['enemyCat']['enemyCatHP'], enemy['enemyCat']['enemyCatHP'], startingHP, f"{missing}")
                elif crit:
                    embed = self.createPVEmbed(ctx, enemy, stat, enemy['enemyCat']['enemyCatHP'], enemy['enemyCat']['enemyCatHP'], startingHP, f"__Enemy cat__ has dealt **{damageDealt} critical damage <:CriticalStrike:884812949343043694>**")
                elif fullGuard:
                    embed = self.createPVEmbed(ctx, enemy, own, enemy['enemyCat']['enemyCatHP'], enemy['enemyCat']['enemyCatHP'], startingHP, f"__{author_cat_name}__ has **put up their gaurd!** Enemy cat only dealt {damageDealt} damage...",)
                else:
                    embed = self.createPVEmbed(ctx, enemy, stat, enemy['enemyCat']['enemyCatHP'], enemy['enemyCat']['enemyCatHP'], startingHP, f"__Enemy cat__ has dealt **{damageDealt} damage**")


                await msg.edit(embed=embed)
                post = stat
                collection.replace_one({'_id':ctx.author.id}, post)
            elif enemyCatSpd == stat['Cats'][0]['SPD'] and random.randint(0, 1) == 1:
                own = collection.find_one({'_id':ctx.author.id})
                author_cat_name = own["Cats"][0]['Name']
                ownStartingHP = own['Cats'][0]['HP']
                stat, missed, crit, fullGuard, damageDealt = self.aiAttackCalc(ctx, enemy, stat, ownStartingHP)
                miss = [f"The enemy cat tripped over a rock a missed their attack", f"The enemy cat stubbed their toe and missed their attack", f"The enemy cat got distracted by a butterfly and missed their attack"]
                missing = random.choice(miss)
                if missed:
                    embed = self.createPVEmbed(ctx, enemy, stat, enemy['enemyCat']['enemyCatHP'], enemy['enemyCat']['enemyCatHP'], startingHP, f"{missing}")
                elif crit:
                    embed = self.createPVEmbed(ctx, enemy, stat, enemy['enemyCat']['enemyCatHP'], enemy['enemyCat']['enemyCatHP'], startingHP, f"__Enemy cat__ has dealt **{damageDealt} critical damage <:CriticalStrike:884812949343043694>**")
                elif fullGuard:
                    embed = self.createPVEmbed(ctx, enemy, own, enemy['enemyCat']['enemyCatHP'], enemy['enemyCat']['enemyCatHP'], startingHP,f"__{author_cat_name}__ has **put up their gaurd!** Enemy cat only dealt {damageDealt} damage...")
                else:
                    embed = self.createPVEmbed(ctx, enemy, stat, enemy['enemyCat']['enemyCatHP'], enemy['enemyCat']['enemyCatHP'], startingHP, f"__Enemy cat__ has dealt **{damageDealt} damage**")

                await msg.edit(embed=embed)


                

                post = stat
                collection.replace_one({'_id':ctx.author.id}, post)
            #post the friendly cat to the friendlly cat db
            await asyncio.sleep(2)
            self.bot.loop.create_task(self.attack(ctx, startingHP, msg, enemyCatHP))
def setup(bot):
    bot.add_cog(RevampedPve(bot))
