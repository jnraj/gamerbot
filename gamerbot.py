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
        
@client.command()
async def pages(ctx):
    contents = ["This is page 1!", "This is page 2!", "This is page 3!", "This is page 4!"]
    pages = 4
    cur_page = 1
    message = await ctx.send(f"Page {cur_page}/{pages}:\n{contents[cur_page-1]}")
    # getting the message object for editing and reacting

    await message.add_reaction("◀️")
    await message.add_reaction("▶️")

    def check(reaction, user):
        return user == ctx.author and str(reaction.emoji) in ["◀️", "▶️"]
        # This makes sure nobody except the command sender can interact with the "menu"

    while True:
        try:
            reaction, user = await client.wait_for("reaction_add", timeout=60, check=check)
            # waiting for a reaction to be added - times out after x seconds, 60 in this
            # example

            if str(reaction.emoji) == "▶️" and cur_page != pages:
                cur_page += 1
                await message.edit(content=f"Page {cur_page}/{pages}:\n{contents[cur_page-1]}")
                await message.remove_reaction(reaction, user)

            elif str(reaction.emoji) == "◀️" and cur_page > 1:
                cur_page -= 1
                await message.edit(content=f"Page {cur_page}/{pages}:\n{contents[cur_page-1]}")
                await message.remove_reaction(reaction, user)

            else:
                await message.remove_reaction(reaction, user)
                # removes reactions if the user tries to go forward on the last page or
                # backwards on the first page
        except asyncio.TimeoutError:
            await message.delete()
            break
            # ending the loop if user doesn't react after x seconds


client.run('ODc4NDY0ODUwODQ0NTg1OTk0.YSBkJQ.9Ebh1g8Z4gvmvBGH5LJwThTMIK8')
