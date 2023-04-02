# ChatGPT-Discord-Bot
I've been searching around for a discord bot that's simple, replies to every message, and is easily configurable. (Whilst also using the cheaper GPT 3.5 Turbo model) But I wasn't able to find any, I only found ones that replied to commands and had no chat history. So I took tidbits of code from everywhere, pieced it together and viola! This code was made for use on Replit btw.

# How can I use ChatGPT 4.0 with this? (PS: this might not work as I have not tested it with GPT-4, as I don't have API access to it)
I'm surprised you're even asking, because anyone with early ChatGPT 4.0 API access should really be more informed about coding than me (I'm a complete amateur!) but here's a way:

Go to the 45th line of code, and change the model from "gpt-3.5-turbo" to "gpt-4" make sure the line of code looks like this:

model="gpt-4",  # The name of the OpenAI chatbot model to use

# How can I start it up as a discord bot?
Good question, I'll try to make the steps nice and tidy, but I'm not that good:

1 - Go to https://discord.com/developers/applications (make sure you're signed in).

2 - Click the top-right button to create a new application, and give it a name.

3 - After creating the application, click on the "Bot" option on the left side of the screen.

4 - Under the "Username" section, you'll find the "Token" section. Click "Copy" to save the bot token somewhere safe for later use.

5 - Back in the "Username" section, choose a name for your bot, which is how it will appear in Discord.

6 - Scroll down to "Privileged Gateway Intents" and turn on all 3 intents.

7 - Click on "OAuth2" on the left side of the page, and then under it: click on "URL Generator".

8 - Under "Scopes", choose the "Bot" scope.

9 - Under "Permissions", select the following permissions: 
"Read Messages/View Channels" under General Permissions, and ALL of the permissions under Text Permissions.

10 - Generate the link and invite the bot to your server of choice.

10.1 Make sure to only give the bot permission to view the channels it needs, to avoid abuse or spam.

Congratulations, you have now successfully created your Discord bot! The next step is to get your OpenAI key, which requires an account on https://openai.com.

# Setting it up from the OpenAI side
1 - Go to https://platform.openai.com/account/api-keys and create a new secret key. Make sure to save this key, as it cannot be retrieved later and you will need it in the setup process.

# Last thing to do is: Set it up on Replit
1 - Head over to https://replit.com/~ and click on "Create Repl" in the top-left corner. Name it however you'd like and choose the template as "Python".

2 - Copy and paste the code from https://raw.githubusercontent.com/Kinatera/ChatGPT-Discord-Bot/main/main.py into the "main.py" file in your Repl.

3 - Edit the "botname", "botchannel", and "botinstructions" variables to customize your bot's name, channel, and instructions. If you're not sure what you're doing, it's best to leave the "botinstructions" variable as is.

4 - On the bottom left of your screen in the Repl, you'll see a lock icon labeled "Secrets". Click on it.

5 - Create four secrets with the following values: "OPENAI_KEY", "OPENAI_KEY2", "DISCORD_TOKEN", and "DISCORD_TOKEN2".

6 - Set the value for "OPENAI_KEY" to the key you saved earlier from step 1 in the OpenAI Setup section.

7 - Set the value for "DISCORD_TOKEN" to the token you saved earlier from step 4 in the Discord Setup section.

8 - Delete the two secrets with "2" at the end of their names, as well as lines 6 and 8 in "main.py", unless you have another OpenAI key or another Discord bot token. If you do, set them as instructed earlier, but now as the "OPENAI_KEY2" secret and the "DISCORD_TOKEN2" secret.

Press "Run" in your Repl and send a message in a Discord channel the bot has access to. Your bot should reply! Have fun :)
