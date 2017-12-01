import discord
import secrets
import timefunctions

from datetime import datetime

client = discord.Client()

# ---commands
command_1 = '!time'  # this command will call the bot
manual = '!help'  # this command will make the bot explain its functionalities

# ---Options
debug = True  # set this to 'True' for more detailed debugging output in console


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

    if debug:
        print('logged into Server(s):')
        for server in client.servers:
            print(server.name, server.id)


@client.event
async def on_message(message):
    if command_1 in message.content and message.author.id != client.user.id:
        bot_message = await client.send_message(message.channel, 'Warping time...')

        time_position = message.content.index(command_1) + len(command_1)  # position of time in the message
        time_string = message.content[time_position + 1:len(message.content)]  # hh:mm
        time = timefunctions.parser(time_string)  # datetime object with possible time zone info

        if debug: print('Time parsed from message: ' + str(time))

        timetable = ''
        delta = timefunctions.delta(time)
        hours, remainder = divmod((timefunctions.delta(time)).seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        # TODO: add a table with common timezones
        #        for tz in timefunctions.TIMEZONES:
        #            timetable = timetable + '    ' + tz

        await client.edit_message(bot_message,
                                  'This is in ' + str(hours) + ' hours and '
                                  + str(minutes) + ' minutes.' + '\n' + timetable)

    if manual in message.content:
        bot_message = await client.send_message(message.channel,
                                                'I can give you a delta to your time. \nCall me with \'!time HH:MM TIMEZONE.\'\n'
                                                'I currently now these time zones: SET (UTC -5), GMT (UTC) and \nCET(UTC + 1))')


client.run(secrets.TOKEN)
