import discord # type: ignore
import os
from dotenv import load_dotenv

import utils


load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$report'):
        try:
            await message.channel.send("Making your report...")

            article_data = utils.get_article_data()
            # if getting the article data raises a timeout error then don't even try to make a summary, just send a message saying there was an
            if article_data == 0:
                raise RuntimeError("Getting article data failed")

            # Generate summary and list
            summary = utils.create_summary(article_data["article"])
            key_terms_str = utils.get_key_terms(article_data["article"])
            key_terms = utils.format_terms(key_terms_str)
            if key_terms == 0:
                raise RuntimeError("Key terms formatting error")
            
            # Send summary and URL to the Discord channel
            await message.channel.send(f"**Headline:**\n{article_data['headline']}")
            await message.channel.send(f"**Summary:**\n{summary}")
            await message.channel.send(f"**Key Political Terms and Concepts:**\n{key_terms}") # TODO: In content: must be 2000... is thrown here
            await message.channel.send(f"**Read more:**\n{article_data['url']}")
        except Exception as e:
            print(f"Error occured: {e}")
            await message.channel.send("Something went wrong, please wait a moment and then try again.")
            

client.run(os.getenv("DISCORD_BOT_TOKEN"))