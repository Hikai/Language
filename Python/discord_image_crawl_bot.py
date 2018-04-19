# -*- coding: utf-8 -*-
from os.path import expanduser, join, isdir
import asyncio
import discord
import requests
import shutil
import threading

client = discord.Client()
path_save = join(expanduser('~'), "Downloads", "Images")


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

            if not isdir(path_save):
                from os import makedirs
                makedirs(path_save)

            if dict_var['filename'].startswith('unknown'):
                ext = dict_var['filename'].split('.')[1]
                dict_var['filename'] = "unknown{}.{}".format(counter, ext)
                counter += 1

            r = requests.get(dict_var['url'], stream=True)
            if r.status_code == 200:
                t = threading.Thread(target=save_file, args=(dict_var['filename'], r))
                t.start()

            else:
                print("Failed {}\n{}".format(r.status_code, dict_var['url']))

        print("End of the image crawl.")


def save_file(name_file, req):
    with open(join(path_save, name_file), "wb") as f:
        req.raw.decode_content = True
        shutil.copyfileobj(req.raw, f)

client.run('token')
