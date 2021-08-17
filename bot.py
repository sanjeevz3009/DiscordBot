import discord
import time
import asyncio
# 877251072220069898

# Branch merge fix!

messages = joined = 0

def readToken():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()
    
token = readToken()

# client = discord.Client()
intents = discord.Intents().all()
client = discord.Client(intents=intents)

async def updateStats():
    await client.wait_until_ready()
    global messages, joined
    
    while not client.is_closed():
        try:
            with open("stats.txt", "a") as f:
                f.write(f"Time : {int(time.time())}, Messages: {messages}, Members Joined: {joined}\n")
            messages = 0
            joined = 0
            
            await asyncio.sleep(5)
        except Exception as e:
            print(e)
            await asyncio.sleep(5)

@client.event
async def on_message(message):
    global messages
    messages += 1
    serverID = client.get_guild(877251072220069898)
    channels = ["commands"]
    validUsers = ["Sanjeev#7455"]
    
    if str(message.channel) in channels and str(message.author) in validUsers:
        if message.content.find("!hello") != -1:
            await message.channel.send("Hi")
        elif message.content == "!users":
            await message.channel.send(f"# of Members: {serverID.member_count}")
    else:
        print(f"User: {message.author} tried to enter a command {message.content}, in channel {message.channel}")
            
@client.event
async def on_member_join(member):
    global joined
    joined += 1
    for channel in member.server.channels:
        if str(channel) == "general":
            await client.send_message(f"Welcome To The Server! {member.mention}")
            
@client.event
async def on_member_update(before, after):
    print("Works")
    n = after.nick
    if n:
        if n.lower().count("sanjeev") > 0:
            last = before.nick
            if last:
                await after.edit(nick=last)
            else:
                await after.edit(nick="NO STOP THAT")
                
            
            
            
client.loop.create_task(updateStats())

client.run(token)