from algosdk.transaction import SuggestedParams
import requests

node_url = 'https://mainnet-api.algonode.cloud'
params_endpoint = '/v2/transactions/params'
url = node_url + params_endpoint

response = requests.get(url)
params_dict  = response.json()

#SuggestedParams must be imported and object created, fee must be 1000 but default is 0 from algonode
params = SuggestedParams(
    fee=1000,
    first=params_dict['last-round'] - 1,
    last=params_dict['last-round'] + 1,
    gh=params_dict['genesis-hash'],
    flat_fee=True
)

print(params)
