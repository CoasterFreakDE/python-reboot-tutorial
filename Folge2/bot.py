import discord

bot = discord.Client(intents=discord.Intents.all())


@bot.event
async def on_ready():
    print(f'BotId: {bot.user.id} - Name: {bot.user.name}')


@bot.event
async def on_raw_reaction_add(payload):
    if payload.member.bot:
        return
    if payload.channel_id == 831955306132668456:
        if payload.message_id == 831955353654394890:
            if payload.emoji.name == '🦷':
                guild: discord.Guild = bot.get_guild(831633094699253831)

                role: discord.Role = guild.get_role(831959844663459850)
                await payload.member.add_roles(role, reason="Zuweisung")

                channel: discord.TextChannel = guild.get_channel(831955306132668456)
                message = await channel.send('Du hast den Zahn gezogen.')
                await message.add_reaction('🦷')


bot.run('Token hier einfügen')
