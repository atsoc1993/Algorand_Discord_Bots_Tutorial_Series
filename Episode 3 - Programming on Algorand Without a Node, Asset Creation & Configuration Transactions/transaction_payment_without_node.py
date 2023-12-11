from algosdk.transaction import PaymentTxn, SuggestedParams
from algosdk.util import algos_to_microalgos
import requests
from algosdk import encoding
import base64

node_url = 'https://mainnet-api.algonode.cloud'
params_endpoint = '/v2/transactions/params'
url = node_url + params_endpoint

response = requests.get(url)
params_dict  = response.json()

#SuggestedParams must be imported and object created, fee must be 1000 but default is 0 for some reason
params = SuggestedParams(
    fee=1000,
    first=params_dict['last-round'] - 1,
    last=params_dict['last-round'] + 1,
    gh=params_dict['genesis-hash'],
    flat_fee=True
)

sender = 'SENDER ADDRESS HERE'

# See get_private_key.py to obtain key from mnemonic phrase or generate new address, mnemonic, and obtain private key
sender_private_key = 'SENDER PRIVATE KEY HERE'

receiver = 'RECEIVER ADDRESS HERE'

amt = algos_to_microalgos(ENTER ALGORAND AMOUNT HERE AS INTEGER) #eg algos_to_microalgos(0.0001)

payment_txn = PaymentTxn(
    sender=sender, sp=params, receiver=receiver, amt=amt, note="Enter a note here if needed otherwise leave blank"
)

signed_payment_tx = payment_tx.sign(sender_private_key)
encoded_tx = encoding.msgpack_encode(signed_payment_tx)
binary_tx = base64.b64decode(encoded_tx)

submit_tx_endpoint = '/v2/transactions'
url = node_url + submit_tx_endpoint
send_transaction = requests.post(url, data=binary_tx)
response = send_transaction.json()

print(response) # Prints transaction ID
