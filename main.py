# IMPORT DISCORD.PY. ALLOWS ACCESS TO DISCORD'S API.
import discord
import os

# GETS THE CLIENT OBJECT FROM DISCORD.PY. CLIENT IS SYNONYMOUS WITH BOT.
bot = discord.Client()

# EVENT LISTENER FOR WHEN THE BOT HAS SWITCHED FROM OFFLINE TO ONLINE.
@bot.event
async def on_ready():
	# CREATES A COUNTER TO KEEP TRACK OF HOW MANY GUILDS / SERVERS THE BOT IS CONNECTED TO.
    guild_count = 0

	# LOOPS THROUGH ALL THE GUILD / SERVERS THAT THE BOT IS ASSOCIATED WITH.
    for guild in bot.guilds:
		# PRINT THE SERVER'S ID AND NAME.
        print(f"- {guild.id} (name: {guild.name})")

		# INCREMENTS THE GUILD COUNTER.
        guild_count = guild_count + 1

	# PRINTS HOW MANY GUILDS / SERVERS THE BOT IS IN.
    print("SampleDiscordBot is in " + str(guild_count) + " guilds.")

# EVENT LISTENER FOR WHEN A NEW MESSAGE IS SENT TO A CHANNEL.
@bot.event
async def on_message(message):
	# CHECKS IF THE MESSAGE THAT WAS SENT IS EQUAL TO "HELLO".
	# if message.content == "hello":
    if message.content.startswith("sunn"):
		# SENDS BACK A MESSAGE TO THE CHANNEL.
        await message.channel.send("suna")
    
@bot.event
async def on_message(message):
    if message.content.lower() in ["haati ka khandala", "hati ka khandaala"]:
        await message.channel.send(file=discord.File('slow-clap-meme.gif'))

@bot.event
async def on_message(message):
    if message.author.id == 965247307362754580:
        await message.channel.send('tameez se')


@bot.event
async def on_message(message):
    if message.content.lower() in ["zinda ho", 'zinda hai', 'still alive', 'are u there']:
        await message.channel.send("I am still alive bro, are you?")


bot.run(os.environ.get("bot_token"))