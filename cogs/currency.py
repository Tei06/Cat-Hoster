import random
from discord.errors import InvalidArgument
import pymongo
import discord
from discord.ext import commands
import asyncio
from utils import helper


bot = discord.Client()


mongo_url = "mongodb+srv://Tei:yeet123LMAO@shizukudb.rt4ys.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
cluster = pymongo.MongoClient(mongo_url)
db = cluster["ShizukuDB"]
collection = db['new']


class Currency(commands.Cog):
    """cat currency system"""
    def __init__(self, bot):
        self.bot = bot


    
    @commands.command(aliases = ['cf'])
    async def coinflip(self, ctx, amount, ht):
        await helper.get_user(ctx.author.id, ctx)
        stats = collection.find_one({"_id":ctx.author.id})
        money = stats['Balance']
        if money < int(amount):
            await ctx.send("You don't have that much money to bet with")
        if ht == "h":
            ht = "heads"
        elif ht == "t":
            ht = "tails"
        if ht == None:
            await ctx.send("You have to guess either __**heads**__ or __**tails**__")
            return
        if int(amount) < 50:
            await ctx.send("You can't bet less than 50 gold")
            return
        win = int(amount) * 1.9
        win_amount = round(win)
        try:
            coins = ['heads', 'tails']
            comp_flip = random.choice(coins)
            if ht == "heads" or "h":
                if comp_flip == "heads":
                    embed=discord.Embed(title="Successful Bet", description = f"Damn. You correctly guessed __**{ht}**__ and won {win_amount}")
                    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/883156757600436344/883156792228581416/heads.gif")
                    await ctx.send(embed=embed)
                    collection.update_one({'_id': ctx.author.id}, {'$inc':{'Balance':win_amount}}, upsert=True)
                elif comp_flip == "tails":
                    embed=discord.Embed(title="Failed Bet", description = f"Try again next time... You incorrectly guessed __**{ht}**__")
                    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/883156757600436344/883156792228581416/heads.gif")
                    await ctx.send(embed=embed)
                    collection.update_one({'_id': ctx.author.id}, {'$inc':{'Balance':-1*win_amount}}, upsert=True)
            elif ht == "tails" or "t":
                if comp_flip == "tails":
                    embed=discord.Embed(title="Successful Bet", description = f"Damn. You correctly guessed __**{ht}**__ and won {win_amount}")
                    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/883156757600436344/883156792228581416/heads.gif")
                    await ctx.send(embed=embed)
                    collection.update_one({'_id': ctx.author.id}, {'$inc':{'Balance':win_amount}}, upsert=True)
                elif comp_flip == "heads":
                    embed=discord.Embed(title="Failed Bet", description = f"Try again next time... You incorrectly guessed __**{ht}**__")
                    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/883156757600436344/883156792228581416/heads.gif")
                    await ctx.send(embed=embed)
                    collection.update_one({'_id': ctx.author.id}, {'$inc':{'Balance':-1*win_amount}}, upsert=True)
        except InvalidArgument:
            await ctx.send("you gotta send a number")


    @commands.command(aliases = ['bal', 'wallet'], brief='The amount of points in your balance')
    async def mypoints(self, ctx, member: discord.Member = None):
        """The amount of points in your balance"""
        await helper.get_user(ctx.author.id, ctx)
        if member == None:
            results = collection.find({'_id':ctx.author.id})
            for result in results:
                amounts = result["Balance"]
                amount = round(amounts)
                await ctx.send(f"**{ctx.author.display_name}'s** Balance: __{amount}__ gold.")
        else:
            await helper.get_user(ctx.author.id, ctx)
            results = collection.find_one({'_id':member.id})
            for result in results:
                amounts = result["Balance"]
                amount = round(amounts)
                await ctx.send(f"**{member.display_name}'s** Balance: __{amount}__ gold.")
            
    @commands.command(brief='give someone points!')
    async def give(self, ctx, member: discord.Member = None, amount = None):
        """give someone points!"""
        await helper.get_user(ctx.author.id, ctx)
        await helper.get_member(member, ctx)
        if member == None:
            await ctx.send(f"{ctx.author.mention} Mention someone to give points to")
        else:
            results = collection.find_one({'_id':ctx.author.id})
            for result in results:
                bal = result['Balance']
            amount = int(amount)
        if amount>bal:
            await ctx.send(f"{ctx.author.mention} You dont have that much to send bruh")
            return
        if amount<0:
            await ctx.send(f"{ctx.author.mention} You can't send someone negative coins")
            return
        if amount == None:
            await ctx.send(f'{ctx.author.mention} enter an amount to give')
            return
        collection.update_one({'_id': ctx.author.id}, {'$inc':{'Balance':-1*amount}}, upsert=True)
        collection.update_one({'_id': member.id}, {'$inc':{'Balance':amount}}, upsert=True)
        await ctx.send(f'{ctx.author.mention} Successfully sent {amount} points to {member.mention}')


    @commands.command(aliases = ['bet'], brief='simply bets points for more points')
    async def gamble(self, ctx, amount):
        """risk your fortune for greater fortune"""
        await helper.get_user(ctx.author.id, ctx)
        amount = int(amount)
        if amount == None:
            await ctx.send(f"{ctx.author.mention} bruh enter how much u want to gamble")
            return
        if amount < 5:
            await ctx.send(f"{ctx.author.mention} you can't bet less than 5 points")
            return
        bank = collection.find_one({'_id': ctx.author.id})
        for m in bank:
            money = m['Balance']
            if money < amount:
                await ctx.send("You don't have that much points in your balance to gamble with")
                return
        else:
            comp_outcomess1 = ['1','2','3','4','5','6','7','8','9','10']
            c_outcome1 = random.choice(comp_outcomess1)
            c_outcome2 = random.choice(comp_outcomess1)
            p_outcome1 = random.choice(comp_outcomess1)
            p_outcome2 = random.choice(comp_outcomess1)
            ct_outcome = int(c_outcome1) + int(c_outcome2)
            pt_outcome = int(p_outcome1) + int(p_outcome2)
            if ct_outcome > pt_outcome:
                em = discord.Embed(description = f"You lost {amount} points. Im actually too good at gambling", colour = discord.Colour(0xec0909))
                em.set_author(name = f"{ctx.author.display_name}'s losing bet")
                em.add_field(name = f"{ctx.author.display_name}'s roll:", value = f"`{p_outcome1}` + `{p_outcome2}` = **{pt_outcome}**")
                em.add_field(name = "Shizuku's roll:".format(bot.user), value = f"`{c_outcome1}` + `{c_outcome2}` = **{ct_outcome}**")
                em.set_footer(text = "lol sucks to suck")
                collection.update_one({'_id': ctx.author.id}, {'$inc':{'Balance':-1*amount}}, upsert=True)
                await ctx.send(embed=em)
            elif ct_outcome < pt_outcome:
                percets = [1, 2, 0.3, 0.4, 0.5, 0.6, 0.8, 0.9, 0.2, 0.25, 0.45]
                percents = random.choice(percets)
                percentss = percents*100
                amount = int(percents*amount)
                em = discord.Embed(description = f"You won {amount} points ({percentss}% of your original bet)", colour = discord.Colour(0x8ff57d))
                em.set_author(name = f"{ctx.author.display_name}'s winning bet")
                em.add_field(name = f"{ctx.author.display_name}'s roll:", value = f"`{p_outcome1}` + `{p_outcome2}` = **{pt_outcome}**")
                em.add_field(name = "Shizuku's roll:".format(bot.user), value = f"`{c_outcome1}` + `{c_outcome2}` = **{ct_outcome}**")
                em.set_footer(text = "gawd dammint i swear u cheated")
                collection.update_one({'_id': ctx.author.id}, {'$inc':{'Balance':amount}}, upsert=True)
                await ctx.send(embed=em)
            elif ct_outcome == pt_outcome:
                em = discord.Embed(description = f"Bruh how did we tie- this shit rigged", colour = discord.Colour(0x8ff57d))
                em.set_author(name = f"how lame...")
                em.add_field(name = f"{ctx.author.display_name} roll:", value = f"`{p_outcome1}` + `{p_outcome2}` = **{pt_outcome}**")
                em.add_field(name = "Shizuku's roll:".format(bot.user), value = f"`{c_outcome1}` + `{c_outcome2}` = **{ct_outcome}**")
                em.set_footer(text = "gawd dammint i swear u cheated")
                await ctx.send(embed=em)
    @commands.command(aliases=["slots"], brief='play slots!')
    async def slot(self, ctx, amount):
        """play slots!"""
        stats = collection.find_one({'_id':ctx.author.id})
        amount = int(amount)
        if stats == None:
            await helper.get_user(ctx.author.id, ctx)
        money = stats['Balance']
        if money < amount:
            await ctx.send(f"{ctx.author.mention} You don't have that much points in your balance bruh")
            return
        if amount < 5:
            await ctx.send(f"{ctx.author.mention} You can't bet less that 5 points")
            return
        if amount < 0:
            await ctx.send(f"{ctx.author.mention} You can't bet negative points bruh")
            return
        """ Roll the slot machine """
        emojis = "🍎🍊🍐🍋🍉🍇🍓🍒"
        a = random.choice(emojis)
        b = random.choice(emojis)
        c = random.choice(emojis)
        slotmachine = f"**[ {a} {b} {c} ]\n{ctx.author.name}**,"
        embed = discord.Embed(title = f"{ctx.author.name}'s Slot Machine!", color = discord.Color.random())
        embed.add_field(name="-----", value = a)
        embed.add_field(name="-----", value = b)
        embed.add_field(name="-----", value = c)
        msg = await ctx.send(embed=embed)
        for i in range(5):
            embed = discord.Embed(title = f"{ctx.author.name}'s Slot Machine!", color = discord.Color.random())
            e = random.choice(emojis)
            f = random.choice(emojis)
            g = random.choice(emojis)
            embed.add_field(name="-----", value = e)
            embed.add_field(name="-----", value = f)
            embed.add_field(name="-----", value = g)
            await asyncio.sleep(0.4)
            await msg.edit(embed=embed)
        if (a == b == c):
            embed9=discord.Embed(title = f"{ctx.author.name}'s Slot Machine!", color = discord.Color.green(),
            description=f"{slotmachine} All matching, you won **50 Points!** 🎉")
            await msg.edit(embed=embed9)
            collection.update({'_id':ctx.author.id}, {'$inc':{'Balance':50}}, upsert=True)
        elif (a == b) or (a == c) or (b == c):
            embed90=discord.Embed(title = f"{ctx.author.name}'s Slot Machine!", color = discord.Color.green(),
            description=f"{slotmachine} Damn you got 2 matchin, you won **10 Points!** 🎉")
            await msg.edit(embed=embed90)
            collection.update({'_id':ctx.author.id}, {'$inc':{'Balance':10}}, upsert=True)
        else:
            embed92=discord.Embed(title = f"{ctx.author.name}'s Slot Machine!", color = discord.Color.red(),
            description=f"{slotmachine} No match, you lost lmao 🎉")
            await msg.edit(embed=embed92)

    @commands.command(brief='owner command only lol')
    async def award(self, ctx, amount):
        amount = int(amount)
        collection.update_one({'_id': ctx.author.id}, {'$inc':{'Balance':amount}}, upsert=True)
        await ctx.send(f'{ctx.author.mention} Successfully awarded {amount} points to {ctx.author.mention}')
    
def setup(bot):
    bot.add_cog(Currency(bot))
    


