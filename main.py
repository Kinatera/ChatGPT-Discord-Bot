import os
import openai
import discord
from dotenv import load_dotenv
TOKEN = os.getenv('DISCORD_TOKEN')
TOKEN2 = os.getenv('DISCORD_TOKEN2')
OPENAI_KEY = os.getenv('OPENAI_KEY')
OPENAI_KEY2 = os.getenv('OPENAI_KEY2')
botname = 'Chatty Lane' # The chatbot's name, change this to your preference.
botchannel = '#bot-talk' # The name of the channel(s) the AI is able respond in, you must configure this from your side on discord aswell, this is only for the AI to understand.
botinstructions = "You are a nice, helpful chatbot named: %s, the server you are on is called, and the name of the channel(s) you are able to respond in are: %s, make sure to serve the users well and answer any questions asked by them in the shortest most informative form possible! Good luck. An additional rule for you is all of your responses may not exceed 2000 characters."%(botname, botchannel) # The instructions the AI will follow.
message_log = [ # This message log is how the AI understands the chat history.
        {"role": "system", "content": botinstructions}]
openai.api_key = OPENAI_KEY2 # This is the OpenAI key that you wish to use, refer  to lines 7 and 8

intents = discord.Intents.all()
intents.typing = True
intents.presences = True

client = discord.Client(command_prefix='!', intents=intents)

@client.event
async def on_ready(): # This function prints something when the bot is active, and set's logged_in_user to the bot's username.
    print(f"Bot has connected to Discord!")
    logged_in_user = client.user

@client.event
async def on_message(message): # This is a function that executes when a message is recieved.

    if message.author == client.user: # If the author is the bot then it will add it's response to the chat history with the role of Assistant(The Chatbot).
      if '' in message.content:
        message_log.append({"role": "assistant", "content": message.content})
        return
    
    if '' in message.content: # If the author is not the bot it will add the user's question/response to the chat history with the role of User.
        message_log.append({"role": "user", "content": message.content})

    response = openai.ChatCompletion.create( # This is the response from the AI, nothing too interesting here, refer to OpenAI's documentation for more information on this.
        model="gpt-3.5-turbo",
        messages=message_log,
        max_tokens=1024,
        stop=None,
        temperature=0.7, # This is how crazy it's responses will be, 0 being the lowest, and 2 being the highest, the recommended temp is already set (0.7), you can experiment if you want.
    )

    r = response.choices[0].message.content # This sets r to the response's contents, if this is not done, the message will be messy.
    await message.channel.send(r) # Sends the response to the channel it was asked a question in.

client.run(TOKEN) # Starts the discord bot using the assigned token in line 5 (In your secrets)
