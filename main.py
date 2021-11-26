import disnake
from disnake.ext import commands
import os
from my_helper import MyHelp

bot=commands.Bot(command_prefix='!', help_command=MyHelp())

for filename in os.listdir(f'./Cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'Cogs.{filename[:-3]}')

bot.run('ODk5NzAyNjYwMzE0MzA4NjE4.YW2nZQ.PqbQpU2v9SBfQjKemXt1ATn05R4')