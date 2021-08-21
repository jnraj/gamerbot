import asyncio
import discord

client = discord.Client()

keywords=["hi", "hello", "sup", "wassup"]
keywords1=["poda", "sheay", "sheri", "pwoli"]
keywords2=["livestream", "live", "stream"]


@client.event                              
async def on_message(message):            
    if message.author == client.user:      
        return                             

    if any(keyword in message.content.lower() for keyword in keywords):
        msg = '{0.author.mention} Hi there! '.format(message)
        await message.channel.send(msg)

    if any(keyword in message.content.lower() for keyword in keywords1):
        msg = '{0.author.mention} Nee poda! '.format(message)
        await message.channel.send(msg)
        
    if any(keyword in message.content.lower() for keyword in keywords2):
        msg = 'Hey {0.author.mention} check out MrGamerRaj's past livestreams <#553394919625195570>! '.format(message)        
        await message.channel.send(msg)

client.run('NTUzOTUxNDQxNDM0NDQzODE2.XIPRew.IG78nUceGKIsQBSviavThc7S2K0')
