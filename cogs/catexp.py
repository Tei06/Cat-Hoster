from os import name
from types import coroutine
from discord import embeds
import pymongo
import discord
from discord.ext import commands


mongo_url = "mongodb+srv://Tei:yeet123LMAO@shizukudb.rt4ys.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
cluster = pymongo.MongoClient(mongo_url)
db = cluster["ShizukuDB"]
collection = db['new']

tiers = {
    "Common": 5,
    "Uncommon": 10,
    "Rare": 20,
    "Epic": 30,
    "Legendary": 100
}
class CatExp(commands.Cog):
    """Ur cats exp lol"""
    def __init__(self, bot):
        self.bot = bot

    async def add_xp(self, ctx, tier):
        cat = collection.find_one({'_id': ctx.author.id})
        cat['Cats'][0]['EXP'] += tiers[tier]
        
        await ctx.send("Your cat gained " + str(tiers[tier]) + "Exp")


        xpNeedForLevelUp = 100
        #leveling up
        for i in range(cat['Cats'][0]['Level']- 1):
            xpNeedForLevelUp = xpNeedForLevelUp * 0.05 + xpNeedForLevelUp
        

        
        valid_reactions = ['1️⃣', '2️⃣', '3️⃣', '4️⃣']
        def check(reaction, user):
            return user == ctx.author and str(reaction.emoji) in valid_reactions


        while cat['Cats'][0]['EXP'] >= xpNeedForLevelUp:
            cat['Cats'][0]['HP'] += 5
            cat['Cats'][0]['Level'] += 1
            cat['Cats'][0]['EXP'] -= xpNeedForLevelUp

            embed = discord.Embed(title="Your Cat Level Up!", descrption="Choose a stat to upgrade! **WARNING**: YOU HAVE 60 SECONDS TO CHOOSE OR ELSE IT WILL NOT ADD ANY UPGRADES")
            embed.add_field(name=":one:", value="Upgrade your HP by 10", inline=False)
            embed.add_field(name=":two:", value="Upgrade your Defense by 5", inline=False)
            embed.add_field(name=":three:", value="Upgrade your Attack by 10", inline=False)
            embed.add_field(name=":four:", value="Upgrade your Speed by 5", inline=False)
            
            msg = await ctx.send(embed=embed)

            await msg.add_reaction("1️⃣")
            await msg.add_reaction("2️⃣")
            await msg.add_reaction("3️⃣")
            await msg.add_reaction("4️⃣")

            
            reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)

            if str(reaction.emoji) == '1️⃣':
                cat['Cats'][0]['HP'] += 10
                await ctx.send("Your cats HP was increased by 10")
            elif str(reaction.emoji) == '2️⃣':
                cat['Cats'][0]['DEF'] += 10
                await ctx.send("Your cats defense was increased by 5")
            elif str(reaction.emoji) == '3️⃣':
                cat['Cats'][0]['ATK'] += 10
                await ctx.send("Your cats attack was increase by 10")
            elif str(reaction.emoji) == '4️⃣':
                cat['Cats'][0]['SPD'] += 5
                await ctx.send("Your cats speed was increased by 5")


        post = cat
        print(post)
        collection.find_one_and_replace({'_id': ctx.author.id}, post)



def setup(bot):
    bot.add_cog(CatExp(bot))