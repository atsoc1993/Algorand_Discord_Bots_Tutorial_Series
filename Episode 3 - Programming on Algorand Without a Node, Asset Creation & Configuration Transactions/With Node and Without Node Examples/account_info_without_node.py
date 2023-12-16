import requests

node_url = 'https://mainnet-api.algonode.cloud'
account_info_endpoint = '/v2/accounts/'

address = 'ENTER ADDRESS HERE'
complete_url = node_url + account_info_endpoint + address

response = requests.get(complete_url)
account_info = response.json()

print(account_info)
