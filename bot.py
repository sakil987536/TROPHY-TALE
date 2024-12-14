import discord
from discord.ext import commands
import firebase_admin
from firebase_admin import credentials, firestore
import json

# Load configuration
with open('config.json') as f:
    config = json.load(f)

# Initialize Firebase
cred = credentials.Certificate("firebase_credentials.json")  # Replace with your Firebase credentials file
firebase_admin.initialize_app(cred)

# Initialize Firestore
db = firestore.client()

# Set up the bot with the proper command prefix and intents
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# Load cogs (modules)
bot.load_extension("cogs.registration")
bot.load_extension("cogs.payment")
bot.load_extension("cogs.bracket")
bot.load_extension("cogs.scoring")

@bot.event
async def on_ready():
    print(f'Bot is logged in as {bot.user}')

# Run the bot with the token from the config file
bot.run(config['token'])
