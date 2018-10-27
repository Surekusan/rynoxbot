from discord.ext import commands

client = commands.Bot(command_prefix="-")
player_dict = dict()


@client.event
async def on_ready():
    print("Bot ist bereit!")


@client.command(pass_context=True)
async def play(ctx, url):
    channel = ctx.message.author.voice.voice_channel
    await client.join_voice_channel(channel)
    server = ctx.message.server
    voice = client.voice_client_in(server)
    player = await voice.create_ytdl_player(url)
    player_dict[server.id] = player
    await client.send_message(ctx.message.channel, "Spielt `%s` ab!" % player.title)
    player.start()


@client.command(pass_context=True)
async def stop(ctx):
    server = ctx.message.server
    player = player_dict[server.id]
    player.stop()
    del player_dict[server.id]


@client.command(pass_context=True)
async def pause(ctx):
    server = ctx.message.server
    player = player_dict[server.id]
    player.pause()


@client.command(pass_context=True)
async def resume(ctx):
    server = ctx.message.server
    player = player_dict[server.id]
    player.resume()


@client.event
async def on_message(message):
    if message.content == "Keks":
        await client.send_message(message.channel, ":cookie:")
    if message.content.upper().startswith('-PING'):
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> Pong!" % (userID))
    if message.content == "Marius":
        await client.send_message(message.channel, ":heart:")
    if message.content.upper().startswith('-SAY'):
        args = message.content.split(" ")
        #args[0] = -SAY
        #args[1] = Hey
        #args[2] = There
        #args[1:] = Hey There
        await client.send_message(message.channel, "%s" % (" ".join(args[1:])))


client.run("NTA1NDExNTUyMTgzMTg5NTA0.DrUCgg.2aWhJ6jjbl0_xuqBz3tVqchvP0s")
