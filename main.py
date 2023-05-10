import discord, random
from discord.ext import commands

TOKEN = "MTA4MjAzOTMyOTM2ODU4NDIwMg.GZn3E0.hfAeEzdV8zsRCSsdCmR6VD7aRM7hdTH92KxabE"

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="$", intents=intents)


@bot.command()
async def roll(ctx):
  d = random.randint(1, 6)
  await ctx.channel.send(f"Rolling a D6 : {d} ")


@bot.command()
async def Ask(ctx, *words):
  st = ""
  for word in words:
    st += word
  if st.endswith("?"):
    await ctx.channel.send("Cool question, I don't know.")
  else:
    await ctx.channel.send("That's not a question")


@bot.command()
async def hello(ctx):
  await ctx.send("Hello! Welcome to the chat.")


@bot.command()
async def compliment(ctx):
  await ctx.send(f"Hello {ctx.author.mention}! You're looking great today!")


questions = [
  'What is your favorite color?',
  'What is the capital of France?',
  'What is the meaning of life?',
  'What is your favorite food?',
  'What is the square root of 64?',
]


@bot.command()
async def question(ctx):
  question = random.choice(questions)
  await ctx.send(question)


@bot.command()
async def meme(ctx):
  meme_url = "when you realize even the end of world is made in China 💀☠️🧟🧨💣"

  await ctx.send(meme_url)


@bot.command()
async def rps(message):

  options = ['rock', 'paper', 'scissors']
  computer_choice = random.choice(options)

  await message.channel.send('Choose your weapon: (rock, paper, scissors)')

  def check(msg):
    return msg.author == message.author and msg.channel == message.channel and msg.content.lower(
    ) in options

  user_choice_message = await bot.wait_for('message', check=check)
  user_choice = user_choice_message.content.lower()

  if user_choice == 'rock' and computer_choice == 'scissors':
    await message.channel.send('You win! I chose scissors.')
  elif user_choice == 'paper' and computer_choice == 'rock':
    await message.channel.send('You win! I chose rock.')
  elif user_choice == 'scissors' and computer_choice == 'paper':
    await message.channel.send('You win! I chose paper.')
  elif user_choice == computer_choice:
    await message.channel.send('It\'s a tie! I also chose ' + computer_choice)
  else:
    await message.channel.send('I win! I chose ' + computer_choice)


bot.run(TOKEN)
