import discord
from discord.ext import commands
from discord.ext.commands import bot

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready(): # on_ready func
    print("The bot is online!")

@bot.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def hello(ctx):
    await ctx.send("sup kiddo :wave:")
    print("A random nerd used the hello command!")

@bot.command()
@commands.cooldown(1, 3, commands.BucketType.user)
@commands.has_role('Admin')
async def ban(ctx, member: discord.Member, content):
    await ctx.send("I Successfully Banned") # send msg in channel
    await member.send(f"You were banned for {content} get rekt") # send dm
    await member.ban() # ban

@bot.command()
@commands.cooldown(1, 3, commands.BucketType.user)
@commands.has_role('Admin')
async def kick(ctx, member: discord.Member, content):
    try:
        await ctx.send("Kicked Them") # send msg in channel
        await member.send(f"You were kicked for {content} get rekt") # send dm
        await member.kick() # kick
    except:
        await ctx.send("Kicked Them")
        await member.kick()

@bot.command()
@commands.has_role('Moderater')
@commands.cooldown(1, 3, commands.BucketType.user)
async def purge(ctx, content):
    amount = int(content) # def amount var
    await ctx.channel.purge(limit=amount + 1) # purge

@bot.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def warn(ctx, content, member: discord.Member):
    await ctx.send("I Warned Them")
    await member.send(f"You were warned for {content}") # send dm

bot.run("NzIyNzUwNTAyNjk3MzA0MDc0.Xunn4g.Qw6rkID2uSLukRlgEPUXjRV8ChI")