import random
import asyncio
import discord
import aiohttp
import json
import os
import re
from discord import Game
from discord.ext.commands import Bot
from googletrans import Translator

BOT_PREFIX = ("?")
TOKEN = ""  

client = Bot(command_prefix=BOT_PREFIX)
translator = Translator()

      
@client.event
async def on_ready():

    print("Logged in as " + client.user.name)


@client.command(pass_context = 1)
async def aide(context):

    embed = discord.Embed(colour=discord.Colour.blue())
    embed=discord.Embed(title="Toutes les commandes !")
    embed.set_author(name="ColorSwap")
    embed.add_field(name="ColorSwap est un bot de Laura :3", value="insta: @laurayasuo | Twitter : @lauratcat", inline=True)

    await client.send_message(context.message.channel, embed=embed)

    embed=discord.Embed(title="Neko")
    embed.add_field(name="?neko", value="Une simple image Neko ^^", inline=False)
    embed.add_field(name="?nekomh", value="Une image Neko :smirk:", inline=False)
    await client.send_message(context.message.channel, embed=embed)

    embed=discord.Embed(title="Fun (je crois)")
    embed.add_field(name="?colorswap", value="Un arc en ciel de pseudo ^^", inline=False)
    embed.add_field(name="?hug", value="Câlin ^^", inline=False)
    embed.add_field(name="?slap", value="Une baffe de l'espace", inline=False)
    embed.add_field(name="?avatar", value="Il est beau ton avatar", inline=False)
    embed.add_field(name="?blague", value="Elles sont pires que google....", inline=False)
    embed.add_field(name="?shifumi", value="https://fr.wikipedia.org/wiki/Pierre-papier-ciseaux", inline=False)
    await client.send_message(context.message.channel, embed=embed)

    embed=discord.Embed(title="Musique")
    embed.add_field(name="?play", value="Joue une musique depuis une url (youtube etc)", inline=False)
    embed.add_field(name="?skip", value="Met la prochaine musique", inline=False)
    embed.add_field(name="?volume", value="Change le volume (normalement)", inline=False)
    await client.send_message(context.message.channel, embed=embed)
    embed=discord.Embed(title="Modo")
    embed.add_field(name="?purge", value="Purge le serveur des messages ^^", inline=False)

    await client.send_message(context.message.channel, embed=embed)


@client.command(pass_context=True, no_pm=True)
async def avatar(ctx, member: discord.Member):
   
    await client.reply("{}".format(member.avatar_url))

#@client.command(pass_context=True, hidden=True)
#async def game(ctx, *, game):
#    game = game.strip()
#    if game != "":
#        try:
#            await self.client.change_presence(game=discord.Game(name=game))
#        except:
#            await client.say("Erreur STG")
#       else:
#            await client.say("Je joue à {}".format(game))

@client.command()
async def invite():

    await client.say("\U0001f44d")
    await client.whisper("https://discordapp.com/oauth2/authorize?client_id=457647478104129547&permissions=335637553&scope=bot")

@client.command(pass_context = 1)
async def neko(context):
    url = 'https://nekos.life/api/v2/img/neko'
    async with aiohttp.ClientSession() as session: 
        try:
            raw_response = await session.get(url)
            response = await raw_response.text()
            response = json.loads(response)
            embed = discord.Embed(colour=discord.Colour.blue())        
            embed.set_image(url=response['url'])
            await client.send_message(context.message.channel, embed=embed)
        except:
            await client.say("Erreur de Traduction")

@client.command(pass_context = 1)
async def blague(context):
    url = 'https://08ad1pao69.execute-api.us-east-1.amazonaws.com/dev/random_joke'
    async with aiohttp.ClientSession() as session: 
        raw_response = await session.get(url)
        messagemodif = await client.send_message(context.message.channel, 'Chargement') 
        response = await raw_response.text()
        response = json.loads(response)
        pronunces = translator.translate(response['setup'], dest='fr')
        await client.edit_message(messagemodif, pronunces.pronunciation)

        await asyncio.sleep(2)
        pronunces = translator.translate(response['punchline'], dest='fr')
        await client.say(pronunces.pronunciation)        



@client.command(pass_context = 1)
async def nekomh(context):
    url = 'https://nekos.life/api/v2/img/lewdk'
    async with aiohttp.ClientSession() as session:  
        raw_response = await session.get(url)
        response = await raw_response.text()
        response = json.loads(response)
        embed = discord.Embed(colour=discord.Colour.blue())        
        embed.set_image(url=response['url'])
        await client.send_message(context.message.channel, embed=embed)
        

@client.command(pass_context = 1)
async def hug(context):
    url = 'https://nekos.life/api/v2/img/hug'
    async with aiohttp.ClientSession() as session:  
        raw_response = await session.get(url)
        response = await raw_response.text()
        response = json.loads(response)
        embed = discord.Embed(colour=discord.Colour.blue())        
        embed.set_image(url=response['url'])
        await client.send_message(context.message.channel, embed=embed)


@client.command(pass_context = 1)
async def shifumi(context):
    foo = [':raised_hand:', ':v:', ':punch:']
    await client.send_message(context.message.channel, 'Shi :left_facing_fist: ')
    await asyncio.sleep(0.5)
    await client.send_message(context.message.channel, 'Fu :left_facing_fist: ')
    await asyncio.sleep(0.5)
    await client.send_message(context.message.channel, 'Mi :left_facing_fist: ')
    await asyncio.sleep(0.5)
    await client.send_message(context.message.channel, random.choice(foo))


@client.command(pass_context = 1)
async def slap(context):
    url = 'https://nekos.life/api/v2/img/slap'
    async with aiohttp.ClientSession() as session:  
        raw_response = await session.get(url)
        response = await raw_response.text()
        response = json.loads(response)
        embed = discord.Embed(colour=discord.Colour.blue())        
        embed.set_image(url=response['url'])
        await client.send_message(context.message.channel, embed=embed)
        
@client.command(pass_context = 1)
async def purge(context, number : int):
    if context.message.author.server_permissions.administrator:

        deleted = await client.purge_from(context.message.channel, limit = number)
        first_message_var = await client.send_message(context.message.channel, '{} message(s) supprimé(s)'.format(len(deleted))) 

        await asyncio.sleep(2)

        await client.delete_message(first_message_var)

@client.command(name='colorswap',
                aliases=['eight_ball', 'eightball', '8-ball'],
                pass_context=True)
async def eight_ball(context):
    await client.wait_until_ready()
    nb_repetitions = 5
    i = 1

    await client.delete_message(context.message)
    await client.send_message(context.message.channel, '<@%s> Pour respecter les réglementations de l\'API de Discord, la commande ?colorswap est limitée à 5 répétitions' % context.message.author.id)
    while i <= nb_repetitions :
        await client.edit_role(context.message.server, context.message.author.roles[1], colour=discord.Colour.blue())
        await asyncio.sleep(0.15)
        await client.edit_role(context.message.server, context.message.author.roles[1], colour=discord.Colour.green())
        await client.edit_role(context.message.server, context.message.author.roles[1], colour=discord.Colour.red())
        await asyncio.sleep(0.15)
        await client.edit_role(context.message.server, context.message.author.roles[1], colour=discord.Colour.orange())
        i = i+1
    await client.edit_role(context.message.server, context.message.author.roles[1], colour=discord.Colour.red())


async def list_servers():
    await client.wait_until_ready()
    while not client.is_closed:
        print("Current servers:")
        for server in client.servers:
            print(server.name)
        await asyncio.sleep(600)








client.remove_command('help')
client.loop.create_task(list_servers())
client.run(TOKEN)

