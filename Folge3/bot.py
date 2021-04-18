import discord
from discord.ext import commands

bot = commands.Bot(intents=discord.Intents.all(), command_prefix='!')


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


@bot.command(name='test')
async def test(ctx, *args):
    await ctx.send(f'Eingabe: {" ".join(args)}')


@bot.command(name='userinfo')
async def userinfo(ctx, member: discord.Member):
    await ctx.send(f'Userinfo für: {member.display_name}')


bot.run('Token hier einfügen')
