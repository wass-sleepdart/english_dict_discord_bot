import disnake
from disnake.ext import commands
from words_API import *
from disnake import Embed


bot=commands.Bot(command_prefix='!')

class Vocabulary(commands.Cog):
    def __init__(self, bot):
        self.bot=bot
    @commands.Cog.listener()
    async def on_ready(self):       
         print('Hello, I am alive')
    @commands.command(aliases=['def', 'define', 'definitions', 'meaning'], description='This command gives you the definition of the word that you input')
    async def definition(self, ctx, word):
        try:
            define=get_definition(word)
            definitions=''
            count=1
            for x in define:
                definitions+='**'
                definitions+=f"{count}. {x['definition']}. "
                definitions+='**'
                definitions+='\n'
                count+=1
            embed=Embed(title=f"Hey {ctx.author.name.title()}, {word} means:", type='rich', description=definitions, color=disnake.Colour.blue())
            await ctx.send(embed=embed)
        except KeyError:
            embed2=Embed(title='I am illiterate', description=f'**sorry I don\'t know what {word} means**' )
            await ctx.send(embed=embed2)
def setup(bot):
    bot.add_cog(Vocabulary(bot))
