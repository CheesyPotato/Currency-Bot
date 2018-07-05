import discord
from discord.ext import commands
from discord import Client


f = open('token.txt', 'r')
token = f.read()
f.seek(0)
f.close()


bot = commands.Bot(command_prefix='!')
client = discord.Client()

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    await client.login(token)
@bot.command(pass_context=True)
async def give(ctx, *arg):
    currencyamount = arg[-1]
    arg = arg[:-1]
    membername = ''
    for argument in arg:
        membername += str(argument) + ' '
    membername = membername[:-1]

    if "currency" in [y.name.lower() for y in ctx.message.author.roles]:
        membername = ctx.message.server.get_member_named(membername)
        if membername == None:
            await bot.say('Error: user not found.')
            return
        membername = membername.name
        f = open('currency.txt', 'r')
        fileread = f.readlines()
        f.seek(0)
        f.close()
        flag = False
        for i in fileread:
            if membername == i[:-1]:
                fileread[fileread.index(i)] = membername + '\n'
                fileread[fileread.index(i) + 1] = str(int(fileread[fileread.index(i) + 1]) + int(currencyamount)) + '\n'
                flag = True
                f = open('currency.txt', 'w')
                f.writelines(fileread)
                f.seek(0)
                f.close()
                break

        if flag == False:
            f = open('currency.txt', 'a')
            f.write(membername + '\n' + currencyamount + '\n')
            f.close()
        await bot.say('$' + str(currencyamount) + ' given to ' + membername + '.')
    else:
        await bot.say('Error: You do not have the "currency" role.')
@bot.command(pass_context=True)
async def show(ctx, *arg):
    if arg == ():
        membername = ctx.message.author.name
    else:
        membername = ''
        for argument in arg:
            membername += str(argument) + ' '
        membername = membername[:-1]
    membername = ctx.message.server.get_member_named(membername)
    if membername == None:
        await bot.say('Error: user not found.')
        return
    membername = membername.name
    f = open('currency.txt', 'r')
    oldfileread = f.readlines()
    f.seek(0)
    f.close()
    fileread = []
    for i in oldfileread:
        fileread.append(i[:-1])
    flag = False

    for i in fileread:
        if membername == i:
            flag = True
            await bot.say(membername + ' has $' + str(fileread[fileread.index(membername) + 1]) + '.')
            break
    if flag == False:
        await bot.say('Error: user not found or user has $0.')
bot.run(token)
