import discord
client = discord.Client()
token = "authXXXX"

blacklist = [
    
]


@client.event
async def on_ready():
    for guild in client.guilds:
        try:
            if guild.id in blacklist:
                server = client.get_guild(guild.id)
                await server.leave()
        except Exception as e:
            print(e)


client.run(token, bot=False)
