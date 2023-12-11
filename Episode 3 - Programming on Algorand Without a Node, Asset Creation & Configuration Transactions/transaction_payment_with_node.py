from algosdk.v2client import *
from algosdk.transaction import PaymentTxn
from algosdk.util import algos_to_microalgos

algod_token = 'ENTER ALGORAND NODE TOKEN HERE'
algod_port = 'http://ENTER ALGORAND NODE PORT HERE'

algod_client = algod.AlgodClient(algod_token, algod_port)


params = algod_client.suggested_params()
sender = 'SENDER ADDRESS HERE'

 # See get_private_key.py to obtain key from mnemonic phrase or generate new address, mnemonic, and obtain private key
sender_private_key = 'SENDER PRIVATE KEY HERE'

receiver = 'RECEIVER ADDRESS HERE'

amt = algos_to_microalgos(ENTER ALGO AMOUNT HERE AS INTEGER) #eg algos_to_microalgos(0.0001)

payment_txn = PaymentTxn(
    sender=sender, sp=params, receiver=receiver, amt=amt, note="Enter a note here if needed otherwise leave blank"
)

signed_payment_txn = payment_txn.sign(sender_private_key)
tx_ID = algod_client.send_transaction(signed_payment_txn)
print(tx_ID) # Prints transaction ID once confirmed
