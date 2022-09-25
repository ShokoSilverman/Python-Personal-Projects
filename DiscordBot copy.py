import discord
import datetime
import json
import requests
import genshinLib as gl

TOKEN = r'OTk3NjQyNTI5OTE2ODY2NTcy.G8t-32.qz6mxiiU4NhMMvW0zTPFIHncUabdbaHyjSwtfc'
GUILD = r"The Coven Of Homies"
client = discord.Client()

@client.event
async def on_ready():
    print('started')
    guild = discord.utils.find(lambda g: g.name == GUILD, client.guilds)

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # await message.channel.send(message.author)

    author: str = str(message.author)
    text: str = str(message.content)
    # attachments: list = [str(i) for i in message.attachments]
    # channel = str(message.channel)

    # command_input: str = '-'.join(command_items[2:])
    if not text.startswith('!genbot'):
    # if command_items[0] != '!genbot':
        # await message.channel.send('test')
        return
    command_items: list = text.split(' ')
    if command_items[1] == 'register':
        if len(command_items) != 5:
            await message.channel.send('wrong number of arguments! should have 3 arguments (uid, ltuid, ltoken)')
            return
        print(command_items[2], command_items[3], command_items[4], author)
        try:
            gl.register(command_items[2], command_items[3], command_items[4], author)
        except:
            await message.channel.send('An error occured, please message Shoko for help')
            return
        await message.channel.send('Registered!')
    elif command_items[1] == 'login':
        gl.login_reward()
        await message.channel.send('daily rewards claimed! <3')
    elif command_items[1] == 'charList':
        if len(command_items) != 3:
            await message.channel.send('Wrong number of arguments, should only have 1 (discord tag)')
            return
        await message.channel.send(gl.character_list(command_items[2]))
    else:
        await message.channel.send('command not recognized!')

        

client.run(TOKEN)