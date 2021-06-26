import discord
from discord import member
import time
# import os
# from dotenv import load_dotenv
# import random
# from discord.ext import commands
# load_dotenv('.env')

# TOKEN = os.getenv("DISCORD_BOT_TOKEN")


intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)
# client = commands.Bot(command_prefix="-")


RULES = "Gentlemen, welcome to Fight Club. \nThe first rule of Fight Club is: You do not talk about Fight Club. \nThe second rule of Fight Club is: You do not talk about Fight Club. \nThird rule of Fight Club: Someone yells \"Stop!\", goes limp, taps out, the fight is over. \nFourth rule: Only two guys to a fight. Fifth rule: One fight at a time, fellas. \nSixth rule: No shirts, no shoes. \nSeventh rule: Fights will go on as long as they have to. \nAnd the eighth and final rule: If this is your first night at Fight Club, you have to fight."
REACTIONS = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣"]
# reactions = [":hand_splayed:", ":hand_fist:", ":v:"]


def createMsg(nxt):
    msg = "Add reactoins:\n"
    emojis = []
    for i in range(len(nxt)):
        msg = msg + str(i) + ". " + nxt[i] + "\n"
        emojis.append(REACTIONS[i])
    return msg, emojis


@client.event
async def on_ready():
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

    if message.content.startswith("-poll"):
        # emojis = []
        nxt = message.content.split(",")
        nxt[0] = nxt[0].split(" ")[1]
        print(nxt)
        msg, emojis = createMsg(nxt)
        print(msg)
        msg_ = await message.channel.send(msg)
        id_ = msg_.id
        for emo in emojis:
            await msg_.add_reaction(emo)
        time.sleep(45)
        getmsg = await message.channel.fetch_message(id_)
        reaction = getmsg.reactions
        print(type(reaction))
        print(reaction)
        max_ = 1
        winner = ""
        winners = []
        j=0
        for react in reaction:
            if react.count > max_:
                max_ = react.count
                winner = nxt[j]
                winners.clear()
                winners.append(nxt[j])

            elif max_ == react.count:
                winners.append(nxt[j])
            j = j+1

        if len(winners) == 1:
            winning_msg = "The winner is: " + winner
            await message.channel.send(winning_msg)
        elif len(winners) != 1:
            winning_msg = "Tie between: "
            for i in winners:
                winning_msg = winning_msg + i + ", "
            await message.channel.send(winning_msg)

    if message.content.startswith("-play"):
        _words = message.content.split(" ")
        print("words", _words)
        nxt = _words[1]
        print(nxt)
        if nxt == "rps":
            print("sleeping")
            time.sleep(5)
            print("awake")
            print('reacts:', message.reactions)
            if(len(message.reactions) == 1):

                print("gotcha")
                user_r = message.reactions[0]
                print(user_r)
                # bot_r = reactions[random.randint(0,2)]
                # message.add_react(bot_r)


# def determine_winner(bot,user):
#     if(bot == user):
#         return 0


# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return

#     if message.content.startswith('-hello there'):
#         await message.channel.send('General Kenobi!')


# @client.command()
# async def hello_there(ctx):
#     await ctx.send("general Kenobi")


client.run('ODQ4MjI3MTQ2MTI3MTE0MjUw.YLJjFg.qgIaCIi37dSGNk0n-DBaJBosXT8')
