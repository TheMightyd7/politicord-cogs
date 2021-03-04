# This init is required for each cog.
# Import your main class from the cog's folder.
from .test import Test


def setup(bot):
    # Add the cog to the bot.
    bot.add_cog(Test())
