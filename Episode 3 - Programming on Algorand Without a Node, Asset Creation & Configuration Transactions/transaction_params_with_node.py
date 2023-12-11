from algosdk.v2client import *

algod_token = 'ENTER ALGORAND NODE TOKEN HERE'
algod_port = 'http://ENTER ALGORAND NODE PORT HERE'

algod_client = algod.AlgodClient(algod_token, algod_port)

params = algod_client.suggested_params()
print(params)


