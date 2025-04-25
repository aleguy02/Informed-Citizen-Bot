# Informed-Citizen-Bot

A Discord bot that fetches the most recent top article from AP News' politics section on request and makes a neat summary of the article and key terms.
## Tech Stack

- Redis Cloud for caching article data.
- Groq for natural language processing.
- Playwright for web scraping.
- BeautifulSoup4 (BS4) for parsing HTML content

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/aleguy02/Informed-Citizen-Bot.git
    cd Informed-Citizen-Bot
    ```

2. Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Configuration

1. Create a `.env` file in the root directory and add the following configuration variables:

    ```env
    DISCORD_TOKEN=your_discord_token
    REDIS_URL=your_redis_url
    GROQ_API_KEY=your_groq_api_key
    ```

2. Ensure you have the required API keys and tokens for Discord, Redis Cloud, and Groq.

## Usage

1. Start the bot:

    ```bash
    python bot.py
    ```

2. Invite the bot to your Discord server using the OAuth2 URL with the `bot` scope and necessary permissions.

3. Use the bot commands in your Discord server to fetch the latest top article from AP News' politics section.
