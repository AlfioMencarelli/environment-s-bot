import random
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Hai fatto l\'accesso come {bot.user}')

lista_pericoli = [
    "Le plastiche nell'oceano si decompongono in piccoli pezzi, che poi i pesci mangiano e arrivano fino al nostro stomaco.",
    "Alcune specie di pesci potrebbero estinguersi per via delle plastiche nell'oceano",
    "Alcune specie animali potrebbero estinguersi perché il loro habitat è stato degradato"
]


@bot.command()
async def pericoli(ctx, tot=1):
    for i in range(tot):
        await ctx.send(random.choice(lista_pericoli))

bot.run("MTE4MjM3NzE3NjA3NTYxNjM1Nw.Grq3H2.lNzmA_EKdROIkm2SxhkfxIVXid3PgqRXOKLhjc")