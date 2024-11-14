import discord # type: ignore
import os
from dotenv import load_dotenv
from get_article_data import get_article_data
from create_summary import create_summary
from get_key_terms import get_key_terms
from parse_response import parse_response

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
            # Fetch article data
            article_data = get_article_data()

            # if getting the article data raises a timeout error then don't even try to make a summary, just send a message saying there was an
            if (article_data != 0):
                # Generate summary and list
                print("working")
                summary = create_summary(article_data["article"])
                key_terms = get_key_terms(article_data["article"])
                print(key_terms)

                # Send summary and URL to the Discord channel
                await message.channel.send(f"**Headline:**\n{article_data['headline']}")
                await message.channel.send(f"**Summary:**\n{summary}")
                # await message.channel.send(f"**Key Political Terms and Concepts:**\n{key_terms}")
                await message.channel.send(f"**Read more:**\n{article_data['url']}")
            else:
                await message.channel.send("Server error occurred. Check your connection and try again later.")
        except Exception as e:
            print(f"Error occured: {e}")
            await message.channel.send("Something went wrong, please try again.")
            

client.run(os.getenv("DISCORD_BOT_TOKEN"))