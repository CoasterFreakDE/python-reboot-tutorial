import discord

bot = discord.Client(intents=discord.Intents.all())


@bot.event
async def on_ready():
    print(f'BotId: {bot.user.id} - Name: {bot.user.name}')


bot.run('DEIN TOKEN EINFüGEN')
