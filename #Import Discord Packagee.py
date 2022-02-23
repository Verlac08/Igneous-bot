#Import Discord Package
from cProfile import run
from itertools import count
from re import X
from turtle import end_fill
import discord
import random
from discord.ext import commands

client = commands.Bot(command_prefix='&')
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('&info for all commands!'))

 

@client.command(name='pick')
async def pick(context):

    picku=['If you were a triangle, you would be a-cute one', 'If I could re-arrange the alphabet then I would put "U" and "I" together', 'Are you a parking ticket ? Cause you got FINE written all over you', 'You sure know how to drive , cause you drove me crazy in love', 'Know what is on the menu ? me "n" u', 'You remind me of 6 letters in the alphabet "u", "r", "a", "q", "t".....silly me thats just 5 of em, You can have the "d" later', 'Are you a magician? Because when I’m looking at you, you make everyone else disappear!','Are you a loan? Because you sure have my interest!', 'Any chance you have an extra heart? Mine’s been stolen!', 'I hope you know CPR, because you just took my breath away!', 'If you were a vegetable, you’d be a ‘cute-cumber.’', 'I believe in following my dreams. Can I have your Instagram?']
    o=str(random.choices(picku))
    k = o.replace("['","")
    p = k.replace("']","")
    await context.message.channel.send(p)

    
@client.command(name='roast')
async def roast(context):
    roastu=['There is someone out there for everyone. For you, its a therapist.', 'If I wanted to kill myself, I would simply jump from your ego to your IQ.', 'Whoever told you to be yourself, gave you a bad advice.', 'Oh please! Shut up if i wanted to hear an asshole speak, I would fart', 'Sorry I can’t think of an insult dumb enough for you to understand.', 'Yes, I’m fully vaccinated, but I will still not hang out with you.', 'You are like a software update. every time I see you, I immediately think “not now"','You were so happy for the negativity of your Covid test, we didn’t want to spoil the happiness by telling you it was IQ test.', 'It is hilarious how you are trying to fit your entire vocabulary into one sentence.',
    'I love what you’ve done with your hair. How do you get it to come out of your nostrils like that?', 'You’re the reason God created the middle finger', 'You bring everyone so much joy! You know, when you leave the room. But, still.', 'I’ll never forget the first time we met. But I’ll keep trying.', 'If your brain was dynamite, there wouldn’t be enough to blow your hat off', 'You are like a cloud. When you disappear, it’s a beautiful day.', 'If you’re going to be two-faced, at least make one of them pretty.', 'I thought of you today. It reminded me to take out the trash.']
    o1=str(random.choices(roastu))
    k1 = o1.replace("['","")
    r = k1.replace("']","")
    await context.message.channel.send(r)

@client.command(name='joke')
async def joke(context):
    jokeu=['What is the difference between a pregnant women and a lightbulb? You can`t unscrew a pregnant women', 'What would the Terminator be called in his retirement? The Exterminator.', 'Why do bees have sticky hair? Because they use a honeycomb.', 'Why is Peter Pan always flying? Because he Neverlands.', 'What do you call a sleeping bull? A bulldozer', 'Why did Ali join tik tok? Because Music-Ali']
    o2=str(random.choices(jokeu))
    k2 = o2.replace("['","")
    j = k2.replace("']","")
    await context.message.channel.send(j)

@client.command(name='darkjoke')
async def darkjoke(context):
    darku=['I was digging in our garden when I found a chest full of gold coins. I was about to run straight home to tell my wife about it . . .but then I remembered why I was digging in our garden.',' Today, I asked my phone “Siri, why am I still single?” and it activated the front camera.', 'Cremation is your last hope to get a smoking hot body', 'Even people who are good for nothing have the capacity to bring a smile to your face, like when you push them down the stairs.', 'What does my dad have in common with Nemo? They both can’t be found.', 'Give a man a match, and he’ll be warm for a few hours. Set him on fire, and he will be warm for the rest of his life.', 'When does a joke become a dad joke? When it leaves you and never comes back.']
    o3=str(random.choices(darku))
    k3 = o3.replace("['","")
    d = k3.replace("']","")
    await context.message.channel.send(d)
    
@client.command('info')
async def info(context):

    
    myEmbed = discord.Embed(title="Info & Commands", description="This bot is in Version 1.5", color=0x00ff00)
    myEmbed.add_field(name="Roast Command", value="Run &roast for epic burns and roasts!", inline=False)
    myEmbed.add_field(name="Pick up lines", value="Run &pick for phenomenal pick up lines that will make you fall head over heels! Thank me later", inline=False)
    myEmbed.add_field(name="TicTacToe", value="Run &tichelp for instructions", inline=False)
    myEmbed.add_field(name="Joke Command", value="Run &joke for hilarious jokes", inline=False)
    myEmbed.add_field(name="Dark Joke Command", value="Run &darkjoke for well you know what", inline=False)
    myEmbed.set_footer(text="Bot is in development & testing phase")
    myEmbed.set_author(name="By Verlac#0001")
     
    await context.message.channel.send(embed=myEmbed)

@client.command(name='tichelp')
async def info(context):

    
    my2Embed = discord.Embed(title="Tic-Tac-Toe", description="Here is how to play tic-tac-toe on this bot", color=0x00ff00)
    my2Embed.add_field(name="How to start", value="Run &tictactoe @user1 @user2 to start", inline=False)
    my2Embed.add_field(name="How to place your mark", value="to place your mark it run place (number) without the brackets so just the number", inline=False)
    my2Embed.add_field(name="Board numbering", value="This is how the board is numbered - https://media.discordapp.net/attachments/945261118769750036/945616773095510016/unknown.png ", inline=False)
    my2Embed.add_field(name="More Games", value="Will be added later", inline=False)
    my2Embed.set_footer(text="Bot is in development & testing phase")
    my2Embed.set_author(name="By Verlac#0001 & Herondale#1631")
    await context.message.channel.send(embed=my2Embed)

player1 = ""
player2 = ""
turn = ""
gameOver = True

board = []

winningConditions = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]

@client.command()
async def tictactoe(ctx, p1: discord.Member, p2: discord.Member):
    global count
    global player1
    global player2
    global turn
    global gameOver

    if gameOver:
        global board
        board = [":white_large_square:", ":white_large_square:", ":white_large_square:",
                 ":white_large_square:", ":white_large_square:", ":white_large_square:",
                 ":white_large_square:", ":white_large_square:", ":white_large_square:"]
        turn = ""
        gameOver = False
        count = 0

        player1 = p1
        player2 = p2

        # print the board
        line = ""
        for x in range(len(board)):
            if x == 2 or x == 5 or x == 8:
                line += " " + board[x]
                await ctx.send(line)
                line = ""
            else:
                line += " " + board[x]

        # determine who goes first
        num = random.randint(1, 2)
        if num == 1:
            turn = player1
            await ctx.send("It is <@" + str(player1.id) + ">'s turn.")
        elif num == 2:
            turn = player2
            await ctx.send("It is <@" + str(player2.id) + ">'s turn.")
    else:
        await ctx.send("A game is already in progress! Finish it before starting a new one.")

@client.command()
async def place(ctx, pos: int):
    global turn
    global player1
    global player2
    global board
    global count
    global gameOver

    if not gameOver:
        mark = ""
        if turn == ctx.author:
            if turn == player1:
                mark = ":regional_indicator_x:"
            elif turn == player2:
                mark = ":o2:"
            if 0 < pos < 10 and board[pos - 1] == ":white_large_square:" :
                board[pos - 1] = mark
                count += 1

                # print the board
                line = ""
                for x in range(len(board)):
                    if x == 2 or x == 5 or x == 8:
                        line += " " + board[x]
                        await ctx.send(line)
                        line = ""
                    else:
                        line += " " + board[x]

                checkWinner(winningConditions, mark)
                print(count)
                if gameOver == True:
                    await ctx.send(mark + " wins!")
                elif count >= 9:
                    gameOver = True
                    await ctx.send("It's a tie!")

                # switch turns
                if turn == player1:
                    turn = player2
                elif turn == player2:
                    turn = player1
            else:
                await ctx.send("Be sure to choose an integer between 1 and 9 (inclusive) and an unmarked tile.")
        else:
            await ctx.send("It is not your turn.")
    else:
        await ctx.send("Please start a new game using the &tictactoe command.")


def checkWinner(winningConditions, mark):
    global gameOver
    for condition in winningConditions:
        if board[condition[0]] == mark and board[condition[1]] == mark and board[condition[2]] == mark:
            gameOver = True

@tictactoe.error
async def tictactoe_error(ctx, error):
    print(error)
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please mention 2 players for this command.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Please make sure to mention/ping players (ie. <@688534433879556134>).")

@place.error
async def place_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please enter a position you would like to mark.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Please make sure to enter an integer.")
    







   

   





client.run('OTQ0OTcwNTgwNjM2MDgyMjI3.YhJWbw.eXufqe4J4gataApdyXRFNKruE68')