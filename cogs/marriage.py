import discord
import asyncio
import pymongo
from utils import emojiSearch, helper
import time
from datetime import date, timedelta
import datetime
from discord.ext import commands


mongo_urls1 = "mongodb+srv://ShizukuTest:yeet123LMAO@cluste.gmxuc.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
clusterr = pymongo.MongoClient(mongo_urls1)
db1 = clusterr["ShizukuTest"]
collec = db1['test']



class Marriage(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(aliases = ['create'])
    async def _marriageaccount(self, ctx):
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
                    "Datetime": [
                        {

                        }
                    ],
                }
        collec.insert_one(marriage_account)
        await ctx.send('Successfully created account')

    @commands.command(aliases = ['propose'])
    async def bond(self, ctx, member: discord.Member):
        authorname = emojiSearch.get_user_name(self, ctx.author.id)
        print(authorname)
        membername = emojiSearch.get_user_name(self, member.id)
        author_acc =  helper.get_user(ctx.author.id, ctx)
        member_acc = helper.get_member(member, ctx)
        if not member_acc:
            return
        elif not author_acc:
            return
        author_stats = collec.find_one({'_id':ctx.author.id})
        member_stats = collec.find_one({'_id':member.id})
        
        if member.id == ctx.author.id:
            embed=discord.Embed(descrpition="Lmao you can't marry yourself", color=discord.Colour(0xf23636))
            await ctx.send(embed=embed)
            return
        if author_stats['Partner'] != None:
            await ctx.send(f"{ctx.author.mention} you are already married to {author_stats['Partner']} <a:animi~10:881364841959419934>")
            return
        elif member_stats['Partner'] != None:
            await ctx.send(f"{ctx.author.mention} {membername} is already married to another person <:F_:881365509503852584>")
            return
        em = discord.Embed(title=f"{authorname} has requested to bond with {membername}", 
        description=f"Type yes (Y) to accept or no (N) to decline",
        color = discord.Colour(0xf23636))
        em.set_thumbnail(url="https://cdn.discordapp.com/emojis/875464343897129000.gif")
        try:
            await ctx.send(embed=em)
            def check(msg):
                return msg.content and msg.channel == ctx.channel and msg.author == member
            msg = await self.bot.wait_for('message', timeout=60.0, check=check)
            yes_list = ['y', 'yes', 'Y', 'Yes', 'YES']
            no_list = ['n', 'no', 'N', 'No', 'NO']
            if any(word in msg.content for word in yes_list):
                embed=discord.Embed(title = "Congratulations!", description = f"**{authorname}** is now happily married to **{membername}** <:woaw:875463342821605386>")
                #<a:dogdance:875461801180037201> <a:dogedance:875461742161977364>
                embed.set_thumbnail(url="https://i.kym-cdn.com/photos/images/original/001/406/781/6e5.gif")
                author_stats['Partner'] = member.id
                author_stats['Name'] = membername
                author_stats['Datetime'] = time.time()
                post = author_stats
                collec.find_one_and_replace({'_id':ctx.author.id}, post)
                member_stats['Partner'] = ctx.author.id
                member_stats['Name'] = authorname
                member_stats['Datetime'] = time.time()
                post1 = member_stats
                collec.find_one_and_replace({'_id':member.id}, post1)
                await ctx.send(embed=embed) 
            elif any(word in msg.content for word in no_list):
                await ctx.send(f"oh damn got rejected")
        except asyncio.exceptions.TimeoutError:
            await ctx.send("ran out of time")   
        except ValueError:
            await ctx.send("https://c.tenor.com/MbitYaN_Oe0AAAAM/kid-bored.gif")
    @commands.command()
    async def divorce(self, ctx):
        pass

    @commands.command(aliases = ['marriage partner','mp'])
    async def marriage_partner(self, ctx):
        author_name = await emojiSearch.get_user_name(self, ctx.author.id)
        stats = collec.find_one({'_id':ctx.author.id})
        partner_name = stats['Name']
        bond_time = round(stats['Datetime'])
        time_together = datetime.timedelta(seconds=round(time.time()) - bond_time)
        await ctx.send(f"**{author_name}** and **{partner_name}** have been together for {time_together}")

    
    @commands.command()
    async def wipe3(self, ctx):
        collec.delete_many({})
        await ctx.send("marriage database wiped")

    @commands.command()
    async def maccount(self, ctx, member: discord.Member = None):
        if member == None:
            author = collec.find_one({'_id':ctx.author.id})
            await ctx.send(author)
        else:
            member = collec.find_one({'_id':member.id})
            await ctx.send(member)

def setup(bot):
    bot.add_cog(Marriage(bot))