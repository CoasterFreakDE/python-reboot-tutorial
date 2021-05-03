import discord
from discord.ext import commands
import pytz
from datetime import datetime

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
    de = pytz.timezone('Europe/Berlin')
    embed = discord.Embed(title=f'> Userinfo für {member.display_name}',
                          description='', color=0x4cd137, timestamp=datetime.now().astimezone(tz=de))

    embed.add_field(name='Name', value=f'```{member.name}#{member.discriminator}```', inline=True)
    embed.add_field(name='Bot', value=f'```{("Ja" if member.bot else "Nein")}```', inline=True)
    embed.add_field(name='Nickname', value=f'```{(member.nick if member.nick else "Nicht gesetzt")}```', inline=True)
    embed.add_field(name='Server beigetreten', value=f'```{member.joined_at}```', inline=True)
    embed.add_field(name='Discord beigetreten', value=f'```{member.created_at}```', inline=True)
    embed.add_field(name='Rollen', value=f'```{len(member.roles)}```', inline=True)
    embed.add_field(name='Höchste Rolle', value=f'```{member.top_role.name}```', inline=True)
    embed.add_field(name='Farbe', value=f'```{member.color}```', inline=True)
    embed.add_field(name='Booster', value=f'```{("Ja" if member.premium_since else "Nein")}```', inline=True)
    embed.set_footer(text=f'Angefordert von {ctx.author.name} • {ctx.author.id}', icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)

bot.run('Dein Bot Token hier')
