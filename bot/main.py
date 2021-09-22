import discord
from discord import member
import time
import os
import reddit
import random
# from dotenv import load_dotenv
# import random
# from discord.ext import commands
# load_dotenv('.env')


intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)
# client = commands.Bot(command_prefix="-")

RULES = "Gentlemen, welcome to Fight Club. \nThe first rule of Fight Club is: You do not talk about Fight Club. \nThe second rule of Fight Club is: You do not talk about Fight Club. \nThird rule of Fight Club: Someone yells \"Stop!\", goes limp, taps out, the fight is over. \nFourth rule: Only two guys to a fight. Fifth rule: One fight at a time, fellas. \nSixth rule: No shirts, no shoes. \nSeventh rule: Fights will go on as long as they have to. \nAnd the eighth and final rule: If this is your first night at Fight Club, you have to fight."
REACTIONS = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣"]
# reactions = [":hand_splayed:", ":hand_fist:", ":v:"]
RPS = ["✊", "🖐️", "✌️"]


def createMsg(nxt):
    msg = "Add reactoins:\n"
    emojis = []
    for i in range(len(nxt)):
        msg = msg + str(i+1) + ". " + nxt[i] + "\n"
        emojis.append(REACTIONS[i])
    return msg, emojis


def rps(a, b):
    if a == b:
        return 0
    elif a == "🖐️" and b == "✊":
        return 1
    elif a == "✊" and b == "🖐️":
        return -1
    elif a == "✌️" and b == "🖐️":
        return 1
    elif a == "🖐️" and b == "✌️":
        return -1
    elif a == "✊" and b == "✌️":
        return 1
    elif a == "✌️" and b == "✊":
        return -1


@client.event
async def on_ready():
    print("hello there")


@client.event
async def on_member_join(member):
    print("joined")
    await member.edit(nick="tylerDurden")
    print("rule sent")
    # await member.send(content=RULES)
    embedVar = discord.Embed(
        title="Gentlemen, welcome to Fight Club.", description="", color=0x0000FF)
    embedVar.add_field(name="The first rule of Fight Club is:",
                       value="You do not talk about Fight Club.", inline=False)
    embedVar.add_field(name="The second rule of Fight Club is",
                       value="You do not talk about Fight Club!", inline=False)
    embedVar.add_field(name="Third rule of Fight Club",
                       value="Someone yells \"Stop!\", goes limp, taps out, the fight is over", inline=False)
    embedVar.add_field(name="Fourth rule",
                       value="Only two guys to a fight", inline=False)
    embedVar.add_field(name="Fifth rule",
                       value="One fight at a time, fellas", inline=False)
    embedVar.add_field(name="Sixth rule",
                       value="No shirt, no shoes", inline=False)
    embedVar.add_field(
        name="Seventh rule", value="Fights will go on as long as they have to", inline=False)
    embedVar.add_field(name="The eighth and final rule",
                       value="If this is your first night at Fight Club, you have to fight.", inline=False)
    await member.send(embed=embedVar)

    # member.nick = "tylerDurden"


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # if message.content.startswith("-help me"):
    #     stepBro = User.id('tylerDurden#3685').format(message)
    #     await message.channel.send("@tylerDurden help me I am stuck")

    if message.content.startswith("u der?"):
        await message.channel.send("yessir")

    if message.content.startswith('>hello'):
            # embedVar = discord.Embed(
            #     title="Hello There", description="General Kenobi", color=0x00ff00)
            # embedVar.add_field(name="Field1", value="hi", inline=False)
            # embedVar.add_field(name="Field2", value="hi2", inline=False)
        await message.channel.send("Hello there")

    if message.content.startswith(">r/"):
        nxt = message.content.split(" ")
        print(nxt)
        if len(nxt) == 2:
            rslash = nxt[1]
            url, title = reddit.getNewPost(rslash)
            await message.channel.send("From " + title+": ")
            await message.channel.send(url)
        elif len(nxt) == 3:
            rslash = nxt[1]
            if nxt[2] == "top":
                url, title = reddit.getTopPost(rslash)
                await message.channel.send("From " + title+" top post: ")
                await message.channel.send(url)
            elif nxt[2] == "new":
                url, title = reddit.getNewPost(rslash)
                await message.channel.send("From " + title+": ")
                await message.channel.send(url)
            elif nxt[2] == "hot":
                url, title = reddit.getNewPost(rslash)
                await message.channel.send("From " + title+" hotest post: ")
                await message.channel.send(url)
            else:
                await message.channel.send("error in command")

        # print(url)
        # await message.channel.send("From " + title+": ")
        # await message.channel.send(url)

    if message.content.startswith(">poll"):
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
        j = 0
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

    if message.content.startswith(">rock paper scissor"):
        _msg = await message.channel.send("React to this msg")
        _id = _msg.id
        for emo in RPS:
            await _msg.add_reaction(emo)
        time.sleep(5)
        getmsg = await message.channel.fetch_message(_id)
        rns = getmsg.reactions
        print(rns)
        count = 0
        voted_reaction = ""
        for react in rns:
            if react.count > count:
                count = react.count
                voted_reaction = react.emoji
        bot_reaction = random.choice(RPS)
        print("bot reaction = " + bot_reaction)
        await _msg.add_reaction(bot_reaction)
        result = rps(voted_reaction, bot_reaction)
        if result == 0:
            await message.channel.send("the bot chose "+bot_reaction+" its a tie")
        elif result == -1:
            await message.channel.send("the bot chose "+bot_reaction + " you lose")
        elif result == 1:
            await message.channel.send("the bot chose "+bot_reaction + " you win")
        print("out of the loop")


client.run(os.environ.get("DISCORD_BOT_TOKEN"))
# client.run(TOKEN)
