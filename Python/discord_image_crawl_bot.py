# -*- coding: utf-8 -*-
import asyncio
import discord
from urllib.request import urlretrieve

client = discord.Client()


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_message(message):
    if message.content.startswith('!test'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            print(log.content)
            if log.author == message.author:
                counter += 1

        await client.edit_message(tmp, 'You have {} messages.'.format(counter))

    elif message.content.startswith('!crawl'):
        async for log in client.logs_from(message.channel, limit=10000):
            if len(log.attachments) <= 0:
                continue

            dict_var = log.attachments[0]
            counter = 0
            if dict_var['filename'].startswith('unknown'):
                ext = dict_var['filename'].split[1]
                dict_var['filename'] = "unknown{}.{}".format(counter, ext)
                counter += 1

            urlretrieve(dict_var['url'], dict_var['filename'])

        print("End of the image crawl.")

client.run('token')
