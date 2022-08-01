# Getting Started

Create a file with '.py ' extension, Like: **main.py**

```python
from btns_menus.Buttons import SButton, SingleButton
from btns_menus.DropMenus import SDropMenu, DuoDropMenu
from btns_menus.Combinations import BtnAndDropMenu, MultiBtnAndMenu

import discord
from discord.ext import commands

intents = discord.Intents.all()
activity = discord.Game("&help - phoenix")

client = commands.Bot(command_prefix="&", intents=intents, activity=activity)


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online)
    print("Bot is Ready !")


@client.command()
async def test(ctx):
    user = ctx.author

    btn1 = SButton(label="Hello", response="Hello have a nice day !")

    view_ = SingleButton(user, btn1).view()
    await ctx.send("click here !", view=view_)


if __name__ == "__main__":
    client.run('token')

```
