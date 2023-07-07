# from .dehoister import Decancer
from .decancer import Decancer

__red_end_user_data_statement__ = (
    "This cog does not persistently store data or metadata about users."
)


async def setup(bot):
    cog = Decancer(bot)
    await cog.initialize()
    await bot.add_cog(cog)
