from algosdk.v2client import *

algod_token = '9225f0a6a3bb74686ed65bc16e06705df9f39a704b77f3c5c6950ca3051431eb'
algod_port = 'http://127.0.0.1:8080'

algod_client = algod.AlgodClient(algod_token, algod_port)

address = 'CQLCW2F3ZTDYQUWPJ2YEZ4HHFU6CLBYZLKV42JK6L6OBXGEBAGEAULQA6E'
account_info_for_address = algod_client.account_info(address)

print(account_info_for_address)
