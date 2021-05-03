# DFP bot
import os
from dotenv import load_dotenv
import asyncio
import random
from discord.ext import commands
import requests
from discord.ext.commands import CommandNotFound

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Update bot version here!
bot_version = '1.0.0'

description = '''DFP bot'''
bot = commands.Bot(command_prefix='/dfp ', description=description)


# Startup
@bot.event
async def on_ready():
    print('Logged in as ' + bot.user.name)
    print('Bot is Ready & is on Version: ' + bot_version)
    r = requests.head("https://defipulse.com")
    print('DeFi Pulse Status code is {}'.format(r.status_code))
    bot.loop.create_task(check_site())


# Talkbacks
say = [
    'Hello World!',
    'BNB is pretty centralized'
]
idk = [
    'Unknown command',
    'Sorry, can you ask me something else?'
]


# SDK keys
sdk_keys = [
    '163930c521fd4032b561476877f924ef',
    'cd28b31424de3f9cfac28b2738725b17',
    '9b7d184c1c2b55f25fdcf252021596f9',
    '0503fa32cee1f7ae60b2f3f22de5aceb',
    'c54de851b08d510e218095981216aebb',
    'eea72f300dadc35f5624af8a078219eb',
    '2c508b7f0a221582e5d42c92014ba323',
    'ef4d48f240d2ac03f2ea9d2f027e62b4',
    'cd6db5d14fc19c1c06579ecd814f64cc',
    '858961ee7a819886481319a60b776d11',
    'fd458477b7b9e8185aa13d0f1743e9c4',
    '70d27bf6c2b13872a0f14fafd0c86db3',
    '7a529df3df7185bd4eaea9158bc3b7ca',
    'f3daa3f31996e68745775905ad78a449',
    'da935881a33a5eb4359a7566accfc871',
    'a73062b0d38e69fa73b582fe027d03fd',
    'e24a64f8ec4a8f776e7ef0ca8c8588a5',
    '77d165b4dc2634da45e0e968060bce41',
    '9b22e239c6bd1d4b319f7b9d984f9111',
    'f63a7d892e8195c24defe29f6882653c',
    'e998726225c753d5505bd07aaa99bd4b',
    'f3ffd899e9045061535d21bf3f9fdb9d',
    'ba3602545762d85eee581b1e6831fe71',
    'bb9665414af475cf0f16d09f1d1b4714',
    'db9f5e6ea237b24d25f041eced4d1dc0'
]

# User IDs
dev = 761644554042474507

mgmt_lookup = {
    # note: use a slice to assign multiple keys to a user
    # example:
    # 229033492707672065: sdk_keys[0:4],
    # assigns keys slot 0, 1, 2, and 3 to Anthony

    229033492707672065: sdk_keys[0:1],  # Anthony
    651262379404820521: sdk_keys[1:2],  # Brian
    473924800356548609: sdk_keys[2:3],  # Arman
    822524778916216882: sdk_keys[3:4],  # Kunle
    326156553382133761: sdk_keys[4:5],  # Nate
    250013912563449856: sdk_keys[5:6],  # Roni
    834496630857793586: sdk_keys[6:7],  # Garrett
    761644554042474507: sdk_keys[7:8]   # TODO add 'Dev' category
    
}

# Channel IDs
eng_alerts = 817509118490837022


# check site
# Potential improvement: create a log file
@bot.event
async def check_site():
    while not bot.is_closed():
        r = requests.head("https://defipulse.com")
        print('DeFi Pulse site status code (https://defipulse.com) is {}'.format(r.status_code))
        channel = bot.get_channel(eng_alerts)
        if r.status_code >= 400:
            await channel.send("<@&{}> Alert! DeFi Pulse site status code (https://defipulse.com) is {}"
                               .format(dev, r.status_code))
            await asyncio.sleep(600)
        else:
            await asyncio.sleep(60)  # wait in seconds


# sup
@bot.command()
async def sup(cmd):
    '''Ask the DFP Bot what\'s up'''
    await cmd.send(say[random.randint(0, len(say)-1)])


# gib
@bot.command()
async def give(cmd, gib, key):
    """Gives SDK keys or DFP status
        Usage: /dfp give sdk_key
        Usage: /dfp give random sdk_key
        Usage: /dfp give status
    """
    print(gib)
    if gib == 'random' and key == 'sdk_key':
        if cmd.author.id in mgmt_lookup:
            await cmd.channel.send(sdk_keys[random.randint(0, len(sdk_keys)-1)])

    elif gib == 'sdk_key':
        if cmd.author.id in mgmt_lookup:
            user = mgmt_lookup[cmd.author.id]
            # grab randomly any of the SDK keys assigned to this user
            await cmd.channel.send(user[random.randint(0, len(user)-1)])
    elif gib == 'status':
        r = requests.head("https://defipulse.com")
        # channel = bot.get_channel(eng_alerts)
        await cmd.send("DeFi Pulse Status code is {}".format(r.status_code))
    else:
        await cmd.send(idk[random.randint(0, len(idk)-1)])


@bot.command()
async def monitor(cmd, site):
    """Monitor any site status code
        Usage: /dfp monitor https://defipulse.com
    """
    r = requests.head(site)
    # channel = bot.get_channel(eng_alerts)
    await cmd.send("Status code of {} is {}".format(site, r.status_code))

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        return
    raise error


# version
@bot.command()
async def version(cmd):
    await cmd.send('This is DFP bot version: ' + bot_version)


bot.run(TOKEN)
