import discord, os, requests, random, string, asyncio
from discord.ext import commands
from keep_alive import keep_alive
from colorama import Fore, Style

def Clear():
    os.system('cls')

Clear()
token = ""
prefix = "&"

client = discord.Client()
client = commands.Bot(command_prefix=prefix,self_bot=True)

@client.event
async def on_ready():
    Clear()
    print(f"Dank Memer Farm V2\nDo {prefix}dankmemer to start bot\n\n")

@client.command(name='dankmemer', aliases=['dank', 'dmc'])
async def dankmemer(ctx): # b'\xfc'
    await ctx.message.delete()
    count = 0
    while True:
        try:
            count += 1
            await ctx.send('pls beg', delete_after=0.1)
            await ctx.send('pls dep max', delete_after=0.1)
            await asyncio.sleep(2.5)
            await ctx.send('pls fish', delete_after=0.1)
            await ctx.send('pls hunt', delete_after=0.1)
            await ctx.send('pls dig', delete_after=0.1)
            print(f'{Fore.BLUE}[DANK-MEMER] {Fore.GREEN}Beg number: {count} sent'+Fore.RESET)
            await asyncio.sleep(46)
        except Exception as e:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)

keep_alive()
client.run(token,bot=False)
