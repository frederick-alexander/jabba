import discord
from discord.ext import commands
import logging
from const import token
from random import randrange, choice

logging.basicConfig(level=logging.WARNING )


jabba_list = []
bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
	print('We have logged in as {0.user}'.format(bot))
	jabba_maker(bot.guilds[0], jabba_list, jabba_list)

@bot.event
async def on_guild_emojis_update(GGN, old, new):
	jabba_maker(GGN, old, new)

def jabba_maker(GGN, old, new):
	old = []
	for item in bot.emojis:
        	if item.name.startswith('jabba'):
                	new.append(item)
	print(new)

@bot.event
async def on_message(message):
    epic = randrange(0,100)
    if message.author == bot.user:
        return
    if epic == 1:
        await message.add_reaction(choice(jabba_list))
    if message.content.startswith('Operation') and message.channel.id == 426108395368611850:
        await message.channel.send('Main Server Content Pack: https://steamcommunity.com/sharedfiles/filedetails/?id=1427363641\n{}\nEvent Server Content Pack: https://steamcommunity.com/sharedfiles/filedetails/?id=1825210078\n{}\nOur Main Server Quickconnect is: steam://connect/104.194.11.250:27050\n{}\nOur Event Server Quickconnect is: steam://connect/104.194.11.250:27055'.format(choice(jabba_list)))

@bot.command()
async def serverinfo(ctx):
	print('Send server info')
	await ctx.send("Main Server: https://cache.gametracker.com/server_info/104.194.11.250:27050/banner_560x95.png?random=35116\n"+
					"Event Server: https://cache.gametracker.com/server_info/104.194.11.250:27055/b_350_20_5a6c3e_383f2d_d2e1b5_2e3226.png")


bot.run(token)
