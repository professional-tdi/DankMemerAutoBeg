import discord, subprocess, sys, time, os, colorama
import json, asyncio, ctypes


from discord.ext import (
    commands,
    tasks
)
from subprocess import call
from itertools import cycle
from colorama import Fore, Back, Style, init

ctypes.windll.kernel32.SetConsoleTitleW('Dank Memer Auto Beg')

with open('config.json') as f:
    config = json.load(f)

token = config.get('token')
prefix = config.get('prefix')

width = os.get_terminal_size().columns
loop = asyncio.get_event_loop()

os.system('mode con: cols=89 lines=22')

colorama.init()
bott = discord.Client()
bott = commands.Bot(
    command_prefix=prefix,
    self_bot=True
)


def startprint():
    
    print(f'''{Fore.RESET}

   ___            __     __  ___                    ___       __         ___          
  / _ \___ ____  / /__  /  |/  /__ __ _  ___ ____  / _ |__ __/ /____    / _ )___ ___ _
 / // / _ `/ _ \/  '_/ / /|_/ / -_)  ' \/ -_) __/ / __ / // / __/ _ \  / _  / -_) _ `/
/____/\_,_/_//_/_/\_\ /_/  /_/\__/_/_/_/\__/_/   /_/ |_\_,_/\__/\___/ /____/\__/\_, / 
                                                                               /___/  
                              
                {Fore.GREEN}======================================================= 
       
                          {Fore.CYAN}Status: {Fore.GREEN}Online
      
      
                          {Fore.CYAN}Prefix: {Fore.GREEN}{prefix}
                          
      
                          {Fore.CYAN}Command: {Fore.GREEN}{prefix}beg  


                          {Fore.CYAN}Tip: {Fore.GREEN}Type {prefix}cls to clear the console after a while
      
                {Fore.GREEN}=======================================================
    '''+Fore.RESET)

def Clear():
    os.system('cls')
Clear()


def Init():
    if config.get('token') == "token-here":
        Clear()
        print(f"{Fore.RED}[ERROR] {Fore.YELLOW}You didnt put your token in the config.json file"+Fore.RESET)
    else:
        token = config.get('token')
        try:
            bott.run(token, bot=False, reconnect=True)
        except discord.errors.LoginFailure:
            print(f"{Fore.RED}[ERROR] {Fore.YELLOW}Token is incorrect."+Fore.RESET)
            os.system('pause >NUL')


def async_executor():
    def outer(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            thing = functools.partial(func, *args, **kwargs)
            return loop.run_in_executor(None, thing)
        return inner
    return outer

startprint()

@bott.command(name='autobeg', aliases=['beg'])
async def _auto_beg(ctx): 
    await ctx.message.delete()
    count = 0
    while True:
        try:
            count += 1 
            await ctx.send('pls beg')           
            print(f'{Fore.BLUE}[AUTO-BEG] {Fore.GREEN}Beg sent: {count}'+Fore.RESET)
            await asyncio.sleep(60)
        except Exception as e:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)     


@bott.command(aliases=['cls'])
async def clearconsole(ctx): # b'\xfc'
    await ctx.message.delete()
    startprint()




if __name__ == '__main__':
    Init()