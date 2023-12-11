import discord
from discord.ext import commands
import json
from algosdk.v2client import *
from algosdk.transaction import PaymentTxn
from algosdk import mnemonic, account
from algosdk.util import microalgos_to_algos, algos_to_microalgos
from discord import Embed

algod_token = 'ENTER YOUR ALGORAND NODE TOKEN HERE'
algod_port = 'ENTER YOUR ALGORAND NODE PORT HERE'

BOT_TOKEN = 'ENTER YOUR DISCORD BOT TOKEN HERE'

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print("Bot is online!")


async def read_registry():
    with open("registry_data.json", "r") as f:
        users = json.load(f)
    return users

async def dump_registry(users):
    with open("registry_data.json", "w") as f:
        json.dump(users, f)
             

@bot.command()
async def ping(ctx):
    '''
    ENTER CHANNEL ID HERE AS AN INTEGER, YOU CAN ALSO REMOVE THE IF STATEMENT TO USE !PING IN ANY CHANNEL
    '''
    if ctx.channel.id == 111111111:
        await ctx.reply("Pong!")
   
@bot.command()
async def register(ctx, algorand_wallet = '0'):
    user_id = str(ctx.author.id)
    user_name = str(ctx.author)
    users = await read_registry()

    
    if algorand_wallet == '0':
        await ctx.reply("Please enter an Algorand address when using this command.\n*Example:* \n*!register F5UX3DAQPBSDF3E3LDTY2AECQZCU7OHQVR4CNM4SQA3BVTXPTGQGW4MYHA*")
        return
    
    elif user_id in users:
        await ctx.reply("You already registered an algorand address")
        return
        
    for all_users in users:
        if users[all_users]["algowallet"] == algorand_wallet:
            await ctx.reply("This algorand address is already registered by another user")
            return
        
        
    try:
        algod_client = algod.AlgodClient(algod_token, algod_port)
        wallet_info = algod_client.account_info(algorand_wallet)
        users[user_id] = {}
        users[user_id]["username"] = user_name
        users[user_id]["algowallet"] = algorand_wallet

        await dump_registry(users)
        await ctx.reply(f"You successfully registered your algorand address! \n{algorand_wallet}")
        
    except Exception as e:
        print(e)
        await ctx.reply("Algorand Address is not valid!")
        
        
@bot.command()
async def pay(ctx):
        
    user = str(ctx.author.id)
    users = await read_registry()
    if user not in users:
        await ctx.reply("You must register first before using this command")
        return
    
    receiver = users[user]["algowallet"] 
    private_key = 'ENTER YOUR PRIVATE KEY HERE IN BASE64, NOT YOUR MNEMONIC' # See get_private_key.py if unsure how to obtain private key
    sender_address = 'ENTER YOUR ADDRESS HERE TO FUND PAYMENTS TO USERS'
    try:
        algod_client = algod.AlgodClient(algod_token, algod_port)
        params = algod_client.suggested_params()

        amt = algos_to_microalgos(0.1)
        payment_tx = PaymentTxn(
            sender_address, params, receiver, amt, note=''
        )
            
        signed_payment_tx = payment_tx.sign(private_key)
        tx_id = algod_client.send_transaction(signed_payment_tx)
        await ctx.reply(f'You received 0.1 Algo to your registered address! \n *Transaction ID: {tx_id}*')
    except Exception as e:
        await ctx.reply(e)
        
        
@bot.command()
async def check_my_algo_balance(ctx):
    
    user = str(ctx.author.id)
    users = await read_registry()
    
    if user not in users:
        await ctx.reply("You must register first before using this command")
        return
    address = users[user]["algowallet"] 
    algod_client = algod.AlgodClient(algod_token, algod_port)
    account_info = algod_client.account_info(address)
    account_balance = account_info['amount']
    account_balance_in_algo = microalgos_to_algos(account_balance)
    await ctx.reply(f'Your current account balance is {account_balance_in_algo}')
    return
        

bot.run(BOT_TOKEN)



