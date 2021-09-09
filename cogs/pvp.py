
import pymongo
import discord
from discord.ext import commands
import random
import asyncio

#enemy
mongo_urls = "mongodb+srv://brian:brianisawesome@cluster0.2tora.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
clusters = pymongo.MongoClient(mongo_urls)
dbs = clusters['ShizukuVouches']
col = dbs['Vouches']

mongo_url = "mongodb+srv://Tei:yeet123LMAO@shizukudb.rt4ys.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
cluster = pymongo.MongoClient(mongo_url)
db = cluster["ShizukuDB"]
collection = db['new']


class Pvp(commands.Cog):
    """fight against bots i guess"""
    def __init__(self, bot):
        self.bot = bot

    def createPVPembed(self, ctx, enemy, own, enemyStartingHP, ownStartingHP, title, author):
        #finds the percentage of filled in boxes
        try:
            if enemy['Cats'][0]['HP'] >= 0:
                enemyPercentage = enemy['Cats'][0]['HP']/enemyStartingHP
            else:
                enemyPercentage = 0
        except:
            enemyPercentage = 0
        enemyBoxes = int(10*enemyPercentage)
        try:
            ourPercentage = own['Cats'][0]['HP']/ownStartingHP
        except:
            ourPercentage = 0
        boxes = int(10*ourPercentage)


        embed = discord.Embed(title=title, description="Its stats are:", colour=discord.Colour(0xff3600))
        embed.set_author(name=author)
        embed.add_field(name="Level", value=enemy['Cats'][0]['Level'])
        embed.add_field(name="HP", value=enemy['Cats'][0]['HP'] )
        embed.add_field(name="Defense", value=enemy['Cats'][0]['DEF'])
        embed.add_field(name="Attack", value=enemy['Cats'][0]['ATK'])
        embed.add_field(name="Speed", value=enemy['Cats'][0]['SPD'])
        embed.add_field(name="HP Bar", value=enemyBoxes * ":red_square:" + (10-enemyBoxes) * ":white_large_square:", inline=False)
        embed.add_field(name="_ _", value="**Our Stats**", inline=False)
        embed.add_field(name="Level", value=own['Cats'][0]['Level'])
        embed.add_field(name="HP", value=own['Cats'][0]['HP'])
        embed.add_field(name="Attack", value=own['Cats'][0]['ATK'])
        embed.add_field(name="Defense", value=own['Cats'][0]['DEF'])
        embed.add_field(name="Speed", value=own['Cats'][0]['SPD'])
        embed.add_field(name="HP Bar", value=boxes * "<:hpfull:882088120823201862>" + (10-boxes) * "<a:hpempty:882082827057917984>", inline=False)

        return embed



    def ownAttackCalc(self, ctx, attacker, defender):
        #evasion calculation
        evasion = defender['Cats'][0]['SPD'] / 5

        if evasion > 60:
            evasion = 60

        chance = random.randint(0, 100)
        
        if chance > evasion:
            if defender['Cats'][0]['DEF'] * 0.75 >= attacker['Cats'][0]['ATK'] * 0.25:
                defender['Cats'][0]['HP'] = defender['Cats'][0]['HP'] - (attacker['Cats'][0]['ATK'] - (attacker['Cats'][0]['DEF']*0.75))
            else:
                defender['Cats'][0]['HP'] = defender['Cats'][0]['HP'] - attacker['Cats'][0]['ATK'] * 0.25
            missed = False
        
        else:
            missed = True
        return defender, missed

    



    async def attack(self, ctx, startingHP, msg, enemyStartingHP, player2ID):
        #enemy db
        enemy = collection.find_one({'_id': player2ID})
        own = collection.find_one({'_id': ctx.author.id})
        print(enemy)
        if enemy != None:
            player2Author = self.bot.get_user(player2ID)
            while True:
                
                
                
                #player 1 attacking
                enemy, missed = self.ownAttackCalc(ctx, own, enemy)
                if missed:
                    embed = self.createPVPembed(ctx, enemy, own, enemyStartingHP, startingHP, "We missed!", ctx.author)
                else:
                    embed = self.createPVPembed(ctx, enemy, own, enemyStartingHP, startingHP, "We attacked!", ctx.author)

                await msg.edit(embed=embed)

                await asyncio.sleep(1)

                #enemy died 
                if enemy['Cats'][0]['HP'] <= 0:
                    #add exp here
                    
                    await ctx.send(f'{ctx.author} You won!')
                    col.delete_one({'_id':ctx.author.id})
                    col.delete_one({"_id":player2ID})
                    own['Cats'][0]['HP'] = startingHP
                    enemy['Cats'][0]['HP'] = enemyStartingHP
                    post = own
                    post2 = enemy
                    collection.replace_one({'_id':ctx.author.id}, post)
                    collection.replace_one({'_id':player2ID}, post2)
                    break
                #did not die, now its their turn!
                else:
                    


                    own, missed = self.ownAttackCalc(ctx, enemy, own)

                    if missed:
                        embed = self.createPVPembed(ctx, enemy, own, enemyStartingHP, startingHP, "We missed!", player2Author)
                    else:
                        embed = self.createPVPembed(ctx, enemy, own, enemyStartingHP, startingHP, "We attacked!", player2Author)

                    await msg.edit(embed=embed)

                    post = own
                    collection.replace_one({'_id':ctx.author.id}, post)
                    

                    #we lost
                    if own['Cats'][0]['HP'] <= 0:
                        #add exp here
                        
                        await ctx.send(f'{player2Author} You won!')
                        col.delete_one({'_id':ctx.author.id})
                        col.delete_one({"_id":player2ID})
                        own['Cats'][0]['HP'] = startingHP
                        enemy['Cats'][0]['HP'] = enemyStartingHP
                        post = own
                        post2 = enemy
                        collection.replace_one({'_id':ctx.author.id}, post)
                        collection.replace_one({'_id':player2ID}, post2)
                        break


                    await asyncio.sleep(1)
        else:
            await ctx.send("You are not in a battle.")

    @commands.command(brief="Fights a cat")
    async def fight2(self, ctx, otherPlayer: discord.User):
        print(type(otherPlayer))
        print(otherPlayer)
        print(otherPlayer.id)

        stat = collection.find_one({'_id': ctx.author.id})
        enemy = collection.find_one({"_id": otherPlayer.id})

        

        print(enemy)
        if stat == None:
            await ctx.send(f"{ctx.author.mention} Please make an account first by doing `-start`", delete_after=10)
        elif enemy == None:
            await ctx.send(f"{ctx.author.mention} Could not find other player", delete_after=10)
        else:
            #spawns a random cat
            startingHP = stat['Cats'][0]['HP']
            otherPlayerStartingHP = enemy['Cats'][0]['HP']

            post = {
                '_id': ctx.author.id,
            }
            post2 = {
                "_id": otherPlayer.id
            }
            col.insert_one(post)
            col.insert_one(post2)
            #embed and stuff

            embed = self.createPVPembed(ctx, enemy, stat, otherPlayerStartingHP, startingHP, "An enemy cat appeared", ctx.author)

            

            msg = await ctx.send(embed=embed)
            
            await asyncio.sleep(1)

            
            if stat['Cats'][0]['SPD'] < enemy['Cats'][0]['SPD']:
                
                
                stat, missed = self.ownAttackCalc(ctx, enemy, stat)
                if missed:
                    embed = self.createPVPembed(ctx, enemy, stat, otherPlayerStartingHP, startingHP, "We missed!", otherPlayer)
                else:
                    embed = self.createPVPembed(ctx, enemy, stat, otherPlayerStartingHP, startingHP, "We attacked!", otherPlayer)



                await msg.edit(embed=embed)
                post = stat
                collection.replace_one({'_id':ctx.author.id}, post)
            elif enemy['Cats'][0]['SPD'] == stat['Cats'][0]['SPD'] and random.randint(0, 1) == 1:


                stat, missed = self.ownAttackCalc(ctx, enemy, stat)
                if missed:
                    embed = self.createPVPembed(ctx, enemy, stat, otherPlayerStartingHP, startingHP, "We missed!", otherPlayer)
                else:
                    embed = self.createPVPembed(ctx, enemy, stat, otherPlayerStartingHP, startingHP, "We attacked!", otherPlayer)

                await msg.edit(embed=embed)


                post = stat
                collection.replace_one({'_id':ctx.author.id}, post)
            #post the friendly cat to the friendlly cat db
            self.bot.loop.create_task(self.attack(ctx, startingHP, msg, otherPlayerStartingHP, otherPlayer.id))



def setup(bot):
    bot.add_cog(Pvp(bot))
