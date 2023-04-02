# ChatGPT-Discord-Bot
I've been searching around for a discord bot that's simple, replies to every message, and is easily configurable. (Whilst also using the cheaper GPT 3.5 Turbo model) But I wasn't able to find any, I only found ones that replied to commands and had no chat history. So I took tidbits of code from everywhere, pieced it together and viola! This code was made for use on Replit btw.

# How can I use ChatGPT 4.0 with this?
I'm surprised you're even asking, because anyone with early ChatGPT 4.0 API access should really be more informed about coding than me (I'm a complete amateur!) but here's a way:
Go to the 45th line of code, and change the model from "gpt-3.5-turbo" to "gpt-4" make sure the line of code looks like this:

model="gpt-4",  # The name of the OpenAI chatbot model to use

# How can I start it up as a discord bot?
Good question, I'll try to make the steps nice and tidy, but I'm not that good:
1 - Go to https://discord.com/developers/applications (and make sure you're signed in)
2 - Make an application by hitting the top-right button and name it however you'd like.
3 - After having created your application, look to the left-side of the screen and press the third option, which should be: "Bot"
4 - This is important, before doing anything else under the section for the username for your bot there's a "Token" section, press copy and save it somewhere safe for a later-on step.
5 - Name your bot however you'd like it to appear as on discord
6 - Scroll down to "Privileged Gateway Intents" and turn on all 3 intents
7 - Click on OAuth2 on the left-hand side of the page, under it should appear two options, pick "URL Generator"
8 - Give it the Bot scope
9 - Give it these following permissions:
General Permissions: Read Messages/View Channels
Text Permissions: All of them
10 - Generate the link and invite the bot to the server of your choosing.
10.1 - Give the bot permission to view only a few channels so the users don't abuse it and spam it, this way you don't lose as many tokens as normal.

You have now successfully made the discord bot, the next step is to get your OpenAI key, which requires an account on https://openai.com

# Setting it up from the OpenAI side
1 - Head over to https://platform.openai.com/account/api-keys and make a new secret key, make sure to save this as you can not get it again and must generate a new key.

# Last thing to do is: Set it up on Replit
So you've made it this far, there are only a few more steps ahead. (PS. Make a replit account or use your google account to sign in)
1 - Head over to https://replit.com/~ and press "Create Repl" in the top-left, name it however you'd like and choose the template as "Python"
2 - Copy and paste the code from https://raw.githubusercontent.com/Kinatera/ChatGPT-Discord-Bot/main/main.py into the replit main.py
3 - Edit the botname, botchannel and botinstructions to however you want. (only touch the botinstructions if you know what you're doing)
4 - On the bottom left of your screen on the replit site, there's a lock key with secrets under it, press it.
5 - Make 4 secrets, with their values being:
OPENAI_KEY
OPENAI_KEY2
DISCORD_TOKEN
DISCORD_TOKEN2
6 - Make the key inside of OPENAI_KEY the key you'd saved before from step 1 in the OpenAI Setup section.
7 - Make the key inside of DISCORD_TOKEN the token you'd saved before from step 4 in the Discord Setup section.
8 - Delete the 2 secrets with a 2 at the end of them unless if you have another OpenAI key or another Discord bot token, set them as instructed previously but now as the OPENAI_KEY2 secret and the DISCORD_TOKEN2 secret.
9 - Press run on replit and send a message in a discord channel the bot has access to, and it should reply! Have fun :)
