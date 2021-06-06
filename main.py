import discord
from discord import member
from discord.ext import commands
import time
import random

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)
# bot = commands.bot(command_prfix = "-")


RULES = "Gentlemen, welcome to Fight Club. \nThe first rule of Fight Club is: You do not talk about Fight Club. \nThe second rule of Fight Club is: You do not talk about Fight Club. \nThird rule of Fight Club: Someone yells \"Stop!\", goes limp, taps out, the fight is over. \nFourth rule: Only two guys to a fight. Fifth rule: One fight at a time, fellas. \nSixth rule: No shirts, no shoes. \nSeventh rule: Fights will go on as long as they have to. \nAnd the eighth and final rule: If this is your first night at Fight Club, you have to fight."

reactions = [":hand_splayed:", ":hand_fist:", ":v:"]

text_channel_list = []
server_list = []


@client.event
async def on_ready():
    # server_list = client.guilds
    # for channel in server_list:
    #     text_channel_list.append(channel.text_channels.name)
    # for server in server_list:
    #     print(server , "\n")
    # for guild in text_channel_list:
    #     print(guild)
    print("hello there")


@client.event
async def on_member_join(member):
    print("joined")
    await member.edit(nick="tylerDurden")
    print("rule sent")
    await member.send(content=RULES)
    # member.nick = "tylerDurden"


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("-are u der?"):
        print("are u der---detected")
        await message.channel.send("yessir")
        
    if message.content.startswith("!play"):
        _words = message.content.split(" ")
        print("words", _words)
        nxt = _words[1]
        print(nxt)
        if nxt == "rps":
            print("sleeping")
            time.sleep(10)
            print("awake")
            print('reacts:', message.reactions)
            if(len(message.reactions) == 1):
                print("gotcha")
                user_r = message.reactions[0]
                print(user_r)
                # bot_r = reactions[random.randint(0,2)]
                # message.add_react(bot_r)




client.run('ODQ4MjI3MTQ2MTI3MTE0MjUw.YLJjFg.qgIaCIi37dSGNk0n-DBaJBosXT8')
