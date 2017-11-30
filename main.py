import discord
import secrets
import timefunctions

from datetime import datetime

client = discord.Client()
command = '!time' #this command will call the bot

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

    print('logged into Server(s):')
    for server in client.servers:
        print(server.name, server.id)

@client.event
async def on_message(message):
    if command in message.content:
        counter = 0
        tmp = await client.send_message(message.channel, 'Warping time...')

        # TODO: get the time out of any message, in any format
        time_position = message.content.index(command) + len(command)       #position of time in the message
        time = message.content[time_position + 1:time_position + 12]         #hh:mm

        print(timefunctions.parse_time(time))

        await client.edit_message(tmp, 'Sick timetable')

        #TODO main functionility here

client.run(secrets.TOKEN)




