import os
import openai
import discord
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set environment variables
TOKEN = os.getenv('DISCORD_TOKEN')
TOKEN2 = os.getenv('DISCORD_TOKEN2')
OPENAI_KEY = os.getenv('OPENAI_KEY')
OPENAI_KEY2 = os.getenv('OPENAI_KEY2')

# Define bot name, channel, and instructions
botname = 'Chatty Lane'
botchannel = '#bot-talk'
botinstructions = "You are a nice, helpful chatbot named: %s, the server you are on is called, and the name of the channel(s) you are able to respond in are: %s, make sure to serve the users well and answer any questions asked by them in the shortest most informative form possible! Good luck. An additional rule for you is all of your responses may not exceed 2000 characters." % (botname, botchannel)

# Initialize message log
message_log = [{"role": "system", "content": botinstructions}]

# Set OpenAI API key
openai.api_key = OPENAI_KEY2

# Set Discord intents
intents = discord.Intents.all()
intents.typing = True
intents.presences = True

# Initialize Discord client
client = discord.Client(command_prefix='!', intents=intents)

# Define on_ready event handler
@client.event
async def on_ready():
    print(f"Bot has connected to Discord!")
    logged_in_user = client.user

# Define on_message event handler
@client.event
async def on_message(message):
    if message.author == client.user:
        # Ignore messages sent by the bot itself
        if '' in message.content:
            # Append bot messages to message log for chat history
            message_log.append({"role": "assistant", "content": message.content})
        return
    # Only consider messages sent by users
    if '' in message.content:
        # Append user messages to message log for chat history
        message_log.append({"role": "user", "content": message.content})
    # Use OpenAI to generate a response
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=message_log,
        max_tokens=1024,
        stop=None,
        temperature=0.7,
    )
    r = response.choices[0].message.content
    # Send the response to the Discord channel
    await message.channel.send(r)

# Start the Discord bot
client.run(TOKEN)
