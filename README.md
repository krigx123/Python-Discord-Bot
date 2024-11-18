
# Python Discord Bot

This is a simple Python Discord bot built using the `discord.py` library. It responds to messages containing the word "Hi" by greeting the user. The bot runs continuously using a Flask server to keep the bot alive.



## Features

- Responds to the word "Hi" with "Hi, I am Rad Bot."
- Runs continuously using a Flask app to keep the bot alive.


## Setup

1.  **Create a Discord Bot** 
   - Go to the [Discord Developer Portal](https://discord.com/developers/applications).
   - Create a new application and add a bot to it.
   - Copy the bot token (you'll need this later).

2.  **Set up the `.env` file:**
   - Create a `.env` file in the root directory of your project and add the following line:
   ```makefile
   DISCORD_BOT_SECRET=your-bot-token-here
   ```
3.  **Run the Bot**
   - Start the bot by running the following command:
   ```bash
   python main.py
   ```


## Deployment

To keep the bot running 24/7, you can deploy it on platforms like Replit. The `keep_alive.py` file ensures that the bot stays alive even when the main bot process doesn't receive requests.

- Create a new Replit project.
- Upload the `main.py` and `keep_alive.py` files.
- Set the `DISCORD_BOT_SECRET` environment variable in the Secrets section of Replit.
- Run the bot with `python main.py`.

