from algosdk.v2client import *

algod_token = 'ENTER ALGORAND NODE TOKEN HERE'
algod_port = 'http://ENTER ALGORAND NODE PORT HERE'

algod_client = algod.AlgodClient(algod_token, algod_port)

address = 'ENTER ALGORAND ADDRESS HERE'
account_info_for_address = algod_client.account_info(address)

print(account_info_for_address)
