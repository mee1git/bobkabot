import config
import discord
import time
from discord.ext import commands
from discord.ext.commands import Bot
from discord.utils import get
from random import randint

prefix = '!'

zeli_bot = Bot(command_prefix=prefix)

Bot.remove_command(zeli_bot, 'help')

@zeli_bot.event
async def on_ready():
    print('Ок')

@zeli_bot.event
async def on_command_error(ctx, error):
    pass

@Bot.command(zeli_bot)
async def hello(ctx):
    author = ctx.message.author
    await ctx.send(f"{author.mention} да-да, Хеллоу, блять... Нахуй иди!")

@Bot.command(zeli_bot)
@commands.has_permissions(administrator=True)
async def set_pupa(ctx, member: discord.Member):
    zelibobka_role = discord.utils.get(ctx.message.guild.roles, name='Zelibobka')
    pupa_role = discord.utils.get(ctx.message.guild.roles, name='Пупа')
    await member.remove_roles(zelibobka_role)
    await member.add_roles(pupa_role)
    await ctx.send(f"{member.mention} стал пупой :C")

@Bot.command(zeli_bot)
@commands.has_permissions(administrator=True)
async def set_zelibobka(ctx, member: discord.Member):
    zelibobka_role = discord.utils.get(ctx.message.guild.roles, name='Zelibobka')
    pupa_role = discord.utils.get(ctx.message.guild.roles, name='Пупа')
    await member.remove_roles(pupa_role)
    await member.add_roles(zelibobka_role)
    await ctx.send(f"{member.mention} стал зелибобкой :)")

@Bot.command(zeli_bot)
@commands.has_permissions(administrator=True)
async def set_bot_inviter(ctx, member: discord.Member):
    bot_inviter_role = discord.utils.get(ctx.message.guild.roles, name='bot_inviter')
    await member.add_roles(bot_inviter_role)
    await ctx.send(f"{member.mention} стал бот_инвайтером, Аеееее, САСНЫЙ!!!")

@Bot.command(zeli_bot)
@commands.has_permissions(administrator=True)
async def del_bot_inviter(ctx, member: discord.Member):
    bot_inviter_role = discord.utils.get(ctx.message.guild.roles, name='bot_inviter')
    await member.remove_roles(bot_inviter_role)
    await ctx.send(f"{member.mention} перестал быть бот_инвайтером :ССССССССС")

@Bot.command(zeli_bot)
@commands.has_role(764864128383975437)
async def join(ctx):
    global voice
    channel = ctx.message.author.voice.channel
    voice = get(zeli_bot.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
        await ctx.send(f'Зелибот присоединился к каналу: {channel}')

@Bot.command(zeli_bot)
@commands.has_role(764864128383975437)
async def leave(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(zeli_bot.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await ctx.send(f'Зелибот решил уйти из канала: {channel}')
        await voice.disconnect()
    else:
        voice = await channel.disconnect()

@Bot.command(zeli_bot)
async def RR(ctx):
    await ctx.send(f'{ctx.author.mention} Крутим барабан...')
    time.sleep(5)
    a = randint(1, 6)
    if a == 1:
        await ctx.send(f'{ctx.author.mention} иди нахуй')
    else:
        await ctx.send(f'{ctx.author.mention}, ну ничего, как-нибудь, в другой раз сходишь нахуй...')


@Bot.command(zeli_bot)
async def clear(ctx, amount=100):
    await ctx.channel.purge(limit=amount+1)

@Bot.command(zeli_bot)
async def help(ctx):
    emb = discord.Embed(title='Список команд Зелибота(Non-admin):', colour=0x2fff00, )
    emb.add_field(name=f'{prefix}help', value='Выводит список команд Зелибота в личные сообщения.', inline=False)
    emb.add_field(name=f'{prefix}hello', value='Зелибот поприветствует вас.', inline=False)
    emb.add_field(name=f'{prefix}clear [Кол-во сообщений]', value='Зелибот удалит 100 сообщений/[Кол-во сообщений]', inline=False)
    emb.add_field(name=f'{prefix}join', value='Пригласить Зелибота в голосовой чат. (Нужно: быть в голосовом чате; иметь роль bot_inviter)', inline=False)
    emb.add_field(name=f'{prefix}leave', value='Выгнать Зелибота из голосового чата. (Нужно: быть в голосовом чате; иметь роль bot_inviter)', inline=False)
    emb.add_field(name=f'{prefix}RR', value='Русская рулетка, шанс 1 к 6 пойти нахуй', inline=False)
    emb1 = discord.Embed(title='Список команд Зелибота(admin):', colour=0x2fff00)
    emb1.add_field(name=f'{prefix}help_in', value='Выводит список команд Зелибота в данный чат', inline=False)
    emb1.add_field(name=f'{prefix}set_pupa [@Пользователь]', value='[@Пользователь] станет пупой.', inline=False)
    emb1.add_field(name=f'{prefix}set_zelibobka [@Пользователь]', value='[@Пользователь] станет зелибобкой', inline=False)
    emb1.add_field(name=f'{prefix}set_bot_inviter [@Пользователь]', value='[@Пользователь] станет бот_инвайтером',
                   inline=False)
    emb1.add_field(name=f'{prefix}del_bot_inviter [@Пользователь]', value='[@Пользователь] перестанет быть бот_инвайтером',
                   inline=False)
    await ctx.message.author.send(embed=emb)
    await ctx.message.author.send(embed=emb1)
@Bot.command(zeli_bot)
@commands.has_permissions(administrator=True)
async def help_in(ctx):
    emb = discord.Embed(title='Список команд Зелибота(Non-admin):', colour=0x2fff00, )
    emb.add_field(name=f'{prefix}help', value='Выводит список команд Зелибота в личные сообщения', inline=False)
    emb.add_field(name=f'{prefix}hello', value='Зелибот поприветствует вас.', inline=False)
    emb.add_field(name=f'{prefix}clear [Кол-во сообщений]', value='Зелибот удалит 100 сообщений/[Кол-во сообщений]', inline=False)
    emb.add_field(name=f'{prefix}join', value='Пригласить Зелибота в голосовой чат. (Нужно: быть в голосовом чате; иметь роль bot_inviter)', inline=False)
    emb.add_field(name=f'{prefix}leave', value='Выгнать Зелибота из голосового чата. (Нужно: быть в голосовом чате; иметь роль bot_inviter)', inline=False)
    emb.add_field(name=f'{prefix}RR', value='Русская рулетка, шанс 1 к 6 пойти нахуй', inline=False)
    emb1 = discord.Embed(title='Список команд Зелибота(admin):', colour=0x2fff00)
    emb1.add_field(name=f'{prefix}help_in', value='Выводит список команд Зелибота в данный чат', inline=False)
    emb1.add_field(name=f'{prefix}set_pupa [@Пользователь]', value='[@Пользователь] станет пупой.', inline=False)
    emb1.add_field(name=f'{prefix}set_zelibobka [@Пользователь]', value='[@Пользователь] станет зелибобкой', inline=False)
    emb1.add_field(name=f'{prefix}set_bot_inviter [@Пользователь]', value='[@Пользователь] станет бот_инвайтером',
                   inline=False)
    emb1.add_field(name=f'{prefix}del_bot_inviter [@Пользователь]', value='[@Пользователь] перестанет быть бот_инвайтером',
                   inline=False)
    await ctx.send(embed=emb)
    await ctx.send(embed=emb1)

@join.error
async def join_error(ctx, error):
    if isinstance(error, commands.MissingRole):
        await ctx.send(f'{ctx.author.mention}, Зелибот не общается с кем попало, для этой команды нужна роль - bot_inviter')

@leave.error
async def leave_error(ctx, error):
    if isinstance(error, commands.MissingRole):
        await ctx.send(f'{ctx.author.mention}, хотел выгнать Зелибота? А может тебя выгнать? Для этой команды нужна роль - bot_inviter')

zeli_bot.run(config.token)
