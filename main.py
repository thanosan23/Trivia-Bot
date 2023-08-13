import os
import random
import html

import requests

import discord
from discord.ext import commands

from dotenv import load_dotenv

import redis

load_dotenv('.env')

leaderboard_db = redis.Redis(host=os.environ['DB_URL'],
                             port=int(os.environ['DB_PORT']),
                             password=os.environ['DB_PASSWORD'])


intents = discord.Intents.all()

bot = commands.Bot(command_prefix= '!', intents=intents)

game_info = { "running": False, "question": None, "correct_answer": None }

def change_score(user : str, change : int):
    global leaderboard_db
    # check if user does not exist in the leaderboard
    if not leaderboard_db.exists(user):
        leaderboard_db.set(user, 0)

    # get the previous score
    previous_score = leaderboard_db.get(user)
    previous_score = int(previous_score.decode('utf-8'))
    # update the new score and update it in the leaderboard
    new_score = previous_score + change
    leaderboard_db.set(user, new_score)

    return new_score

@bot.event
async def on_ready():
    print(f"Bot {bot.user} is ready!")

@bot.slash_command(name="hello")
async def hello(ctx):
    await  ctx.respond("Hello!")

@bot.command()
async def trivia(ctx : commands.Context):
    global game_info
    if not game_info["running"]:
        data = requests.get("https://opentdb.com/api.php?amount=1&type=multiple")
        json = data.json()

        # parse the request output
        result = json['results'][0]

        question = result["question"]

        correct_answer = result["correct_answer"]
        incorrect_answers = result["incorrect_answers"]

        # decode html entities
        question = html.unescape(question)
        correct_answer = html.unescape(correct_answer)
        incorrect_answers = [ html.unescape(answer) for answer in incorrect_answers ]

        # shuffle all the answers
        answers = []
        answers.extend([correct_answer])
        answers.extend(incorrect_answers)
        random.shuffle(answers)

        # create an embed
        embed = discord.Embed(title=question)

        for i in range(len(answers)):
            if answers[i] == correct_answer:
                game_info["correct_answer"] = chr(ord('a') + i)
            embed.add_field(name=f"Option {chr(ord('A')+i)}", value=answers[i])

        game_info["question"] = question

        game_info["running"] = True

        await ctx.send(embed=embed)
    else:
        await ctx.send("Trivia question already exists!")

@bot.command()
async def pick(ctx : commands.Context, choice : str):
    global game_info

    if game_info["running"]:
        choice = choice.lower()

        if choice not in ['a', 'b', 'c', 'd']:
            await ctx.reply("Invalid answer!")
        else:
            if choice == game_info["correct_answer"]:
                await ctx.reply("Congrats! That is the right answer!")
                game_info["running"] = False
                game_info["question"] = None
                game_info["correct_answer"] = None
                change_score(ctx.author.name, 1)
            else:
                await ctx.reply("That is the wrong answer!")
    else:
        await ctx.reply("Someone already solved the trivia question!")


@bot.command()
async def score(ctx : commands.Context):
    global leaderboard_db
    if not leaderboard_db.exists(ctx.author.name):
        leaderboard_db.set(ctx.author.name, 0)
    score = leaderboard_db.get(ctx.author.name)
    score = int(score.decode('utf-8'))
    await ctx.send(f"Your score is: {score}!")


if __name__ == "__main__":
    bot.run(os.environ['DISCORD_TOKEN'])
