from algosdk.v2client import *
from algosdk.transaction import AssetCreateTxn
import json

algod_token = 'YOUR ALGORAND NODE TOKEN'
algod_port = 'http://YOUR PORT GOES HERE'

def create_asset(complete_template, url_for_IPFS, asset_name, asset_unit):
    algod_client = algod.AlgodClient(algod_token, algod_port)
    sender_address = 'Your Algorand Address Here' # This will be the creator address
    sender_private_key = 'Your Private Key in Base64' # See get_private_key.py if you do not have your private key
    params = algod_client.suggested_params()
    
    asset_creation_tx = AssetCreateTxn(
        sender=sender_address,
        sp = params, 
        total=1,
        decimals=0,
        default_frozen= False,
        manager=sender_address,
        reserve=sender_address, 
        freeze=None, 
        clawback=None,
        asset_name=asset_name,
        unit_name=asset_unit,
        url=url_for_IPFS,
        note=json.dumps(complete_template).encode(),
    )
    signed_asset_creation_tx = asset_creation_tx.sign(sender_private_key)
    return algod_client.send_transaction(signed_asset_creation_tx)

#Example Usage

# See template_creation.py
complete_template = {'Your Metadata Here} 

# See upload_to_ipfs.py
url_for_IPFS = 'https://ipfs.io/ipfs/your_hash_goes_here' 

# Asset Name
asset_name = 'Ash Maker' 

# Unit Name
asset_unit = 'PK#1' 

# Call the create_asset function with arguments as metadata template, IPFS url linking to image, asset name and asset unit for ARC-69 standard NFT
transaction_ID = create_asset(complete_template, url_for_IPFS, asset_name, asset_unit)
print(transaction_ID)

