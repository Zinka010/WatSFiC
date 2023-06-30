import discord
from discord.ext import commands
from discord.ext.commands import has_permissions

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='.', intents=intents)

# This command will kick all users with no roles
# Run with .kicknorole
# Admin priveleges are required
@bot.command()
@has_permissions(administrator=True)
async def kicknorole(ctx: commands.Context):
    members = ctx.guild.members
        
    for member in members:
        if len(member.roles) == 1:
            await member.kick()
            print(member.name)
    await ctx.reply('Done!')

bot.run('MTEyNDM4ODAzMzUzMDE3MTQyMg.G-y1wQ.ftm6wNkajLTWsAyT9h8mthp1XPL0bnbo9tqdTs')
