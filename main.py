import os
import discord
from discord.ext import commands

bobka = commands.Bot(command_prefix='.')

@bobka.event
async def on_ready():
    print("Работаем!")

    await bobka.change_presence(status=discord.Status.online, activity=discord.Game(" выдачу роли Пупа"))

    chn = bobka.get_channel(765206913138163714)
    txt = "Тыкни на реакцию и станешь пупой:wink:"
    msg = await chn.send(txt)
    await msg.add_reaction(emoji="💩")

@bobka.event
async def on_reaction_add(reaction, member):
    chn = bobka.get_channel(765206913138163714)
    if reaction.message.channel.id != chn.id:
        print('Hui')
        return
    if reaction.emoji == "💩":
        role = discord.utils.get(member.guild.roles, name="Пупа")
        await member.add_roles(role)

bobka.run(os.environ['TOKEN2'])

# wow it is comment
