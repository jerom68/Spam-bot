import discord
import asyncio
import os
import random
from flask import Flask

# Discord Bot Setup
intents = discord.Intents.all()  # Enable all intents
client = discord.Client(intents=intents)

# Flask Web Server (For Render)
app = Flask(__name__)

@app.route('/')
def home():
    return "✅ Bot is running!"

# Get Environment Variables
TOKEN = os.getenv("DISCORD_TOKEN")  # Bot Token from Render
CHANNEL_ID = int(os.getenv("CHANNEL_ID", "0"))  # Channel where the bot will send messages
PORT = int(os.getenv("PORT", "8080"))  # Port for Render

# Messages List
MESSAGES = [
    "**🔥 Anyone excited for a rare Pokémon? 🔥**",
    "__⚡ Who will spawn next? Place your guesses! ⚡__",
    "**💎 Hope nfjsnfnkancnksncnsksmcnkakdndkkanckskxbxjskcnjxksncjskxndjksnxjdkcnkdksnxksncnskkdnxjskxncjksnxjxjskxnjxksndjxksnxjdkbcjdjdn you please fjdjdthis is a good ur name senpai best friend so much time will you be there 😍 to you and the bis  the name of continents in the server z is not working properly zthe zzis the zza of ZZ the bot and zfan of u and zzis z💎**",
    "__🎯 Let's keep chatting and spawning Pokémon! 🎯__",
    "**🌀 Has anyone caught a legendary recently?**",
]

@client.event
async def on_ready():
    print(f"✅ Logged in as {client.user}!")
    await send_messages()

async def send_messages():
    await client.wait_until_ready()
    channel = client.get_channel(CHANNEL_ID)

    if not channel:
        print("⚠️ Invalid channel ID!")
        return

    while True:
        message = random.choice(MESSAGES)
        await channel.send(message)
        print(f"✅ Sent message: {message}")
        await asyncio.sleep(random.randint(20, 60))  # Random interval to avoid spam

if __name__ == "__main__":
    from threading import Thread
    bot_thread = Thread(target=client.run, args=(TOKEN,))
    bot_thread.start()
    app.run(host="0.0.0.0", port=PORT)
