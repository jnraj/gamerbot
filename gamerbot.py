import asyncio
import discord

client = discord.Client()

keywords1=["hi", "hello", "sup", "wassup"]
keywords2=["poda", "sheay", "sheri", "pwoli"]
keywords3=["livestream", "live", "stream"]
keywords4=["morning"]
keywords5=["evening"]
keywords6=["night"]
keywords7=["onam"]


@client.event                              
async def on_message(message):            
    if message.author == client.user:      
        return                             
    
    if any(keyword in message.content.lower() for keyword in keywords1):
        msg = '{0.author.mention} Hi there! '.format(message)
        await message.channel.send(msg)   
    
    if any(keyword in message.content.lower() for keyword in keywords2):
        msg = '{0.author.mention} Nee poda! '.format(message)
        await message.channel.send(msg) 
    
    if any(keyword in message.content.lower() for keyword in keywords3):
        msg = 'Hey {0.author.mention} check out MrGamerRajs past livestreams <#553394919625195570>! '.format(message)        
        await message.channel.send(msg)
        
    if any(keyword in message.content.lower() for keyword in keywords4):
        msg = '{0.author.mention} Good morning! '.format(message)
        await message.channel.send(msg) 
        
    if any(keyword in message.content.lower() for keyword in keywords5):
        msg = '{0.author.mention} Good evening! '.format(message)
        await message.channel.send(msg) 
        
    if any(keyword in message.content.lower() for keyword in keywords6):
        msg = '{0.author.mention} Good night! '.format(message)
        await message.channel.send(msg)
        
    if any(keyword in message.content.lower() for keyword in keywords7):
        msg = '{0.author.mention} Wishing you a very happy and prosperous Onam! '.format(message)
        await message.channel.send(msg) 


client.run('ODc4NDY0ODUwODQ0NTg1OTk0.YSBkJQ.9Ebh1g8Z4gvmvBGH5LJwThTMIK8')
