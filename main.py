import time
import discord
from discord.ext import commands
from discord.utils import get

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(intents=intents, command_prefix="-")
bot.remove_command("help")




TOKEN = ''

@bot.event
async def on_ready():
    print('Logged in as: ' + bot.user.name)
    print('Ready!\n')

@bot.event
async def on_member_join(member):
    embed = discord.Embed(title="Welcome " + str(member), color=0xff0000)
    embed.set_author(name="Welcome", icon_url="https://www.williamd47.net/hdlogoremastered.png")
    embed.set_footer(text="Welcome to the server!")
    channel1 = bot.get_channel(id=812392527474851855)
    await channel1.send(embed=embed)
    role = get(member.guild.roles, id=812392527108767756)
    await member.add_roles(role)
    await lookForTimes(member, get(member.guild.roles, id=812392527108767756))


async def lookForTimes(member, role):
    time.sleep(604800)
    await member.add_roles(role)

@bot.command()
async def ping(ctx):
     await ctx.send(f'Pong! In {round(bot.latency * 1000)}ms')


@bot.command()
async def clear(ctx, amount=0):
    if ctx.message.author.guild_permissions.administrator or ctx.message.author.guild_permissions.manage_messages:
        if amount != 0:
            amount += 1
            await ctx.channel.purge(limit=amount)
            amount -= 1
            await ctx.channel.send(":white_check_mark: Cleared **" + str(amount) + "** messages!", delete_after=5)
        else:
            await ctx.channel.send(":x: You need to specify a valid number", delete_after=5)
    else:
        await ctx.channel.send(":x: You do not have the permissions!", delete_after=5)



@bot.command(pass_context=True)
async def kick(ctx, userName: discord.Member = "no", *, reason="No reason specified"):
    if ctx.message.author.guild_permissions.administrator:
        if userName == "no":
            await ctx.send(":x: You need to specify a member", delete_after=5)
        else:
            channel = await userName.create_dm()
            await channel.send(f"You were kicked from **{ctx.guild.name}** for *{reason}*")
            await userName.kick(reason=reason)
            await ctx.send(":mechanical_leg: Kicked **" + str(userName) + "** for " + reason, delete_after=5)
    else:
        await ctx.channel.send(":x: You do not have the permissions!", delete_after=5)



@bot.command(pass_context=True)
async def ban(ctx, userName: discord.Member = "no", *, reason="No reason specified"):
    if ctx.message.author.guild_permissions.administrator:
        if userName == "no":
            await ctx.send(":x: You need to specify a member", delete_after=5)
        else:
            channel = await userName.create_dm()
            await channel.send(f"You were banned from **{ctx.guild.name}** for *{reason}*")
            await userName.ban(reason=reason)
            await ctx.send(":hammer: Banned **" + str(userName) + "** for " + reason, delete_after=5)
    else:
        await ctx.channel.send(":x: You do not have the permissions!", delete_after=5)




bot.run(TOKEN)
