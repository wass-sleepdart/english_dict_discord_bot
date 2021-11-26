import disnake
from disnake.ext import commands
from disnake.ext.commands import MinimalHelpCommand

class MyHelp(MinimalHelpCommand):
    async def send_pages(self):
        destination=self.get_destination()
        for page in self.paginator.pages:
            embed=disnake.Embed(description=page, color=disnake.Color.blurple())
            await destination.send(embed=embed)
            
