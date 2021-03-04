from redbot.core import commands


# Classname should be CamelCase and the same spelling as the folder
class TestCog(commands.Cog):

    @commands.command()
    async def test(self, ctx):
        await ctx.send("Hello world")
