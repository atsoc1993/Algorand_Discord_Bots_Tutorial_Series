import requests
from algosdk.transaction import SuggestedParams, AssetCreateTxn
import json


infura_IPFS_api_key = 'Your Infura API Key Here'
infura_IPFS_api_secret = 'Your Infura Secret Here'
infura_IPFS_url = 'https://ipfs.infura.io:5001/api/v0/add'

# This function creates and returns a metadata template with an empty dictionary as the value for the properties key
# This is called when running the fill_template function
def create_template():
    return {
        "standard": "arc69",
        "mime_type": "image/jpg",
        "properties": {}
    }

# This function accepts arguments for your assets attributes, these will be in the metadata and can be adjusted at your preference by adding or removing key/value pairs in the dictionary and arguments
# This function returns a complete metadata template
def fill_template(name, description, type, strength, health, level, exp):
    template = create_template()
    template["properties"] = {
        "Name": name,
        "Description": description,
        "Type": type,
        "Strength": strength,
        "Health": health,
        "Level": level,
        "Experience": exp
    }
    return template

# This function uploads your image (must be in the same folder as this python file) to IPFS, and returns a link to where your image is hosted on IPFS
def upload_to_ipfs(image_path):
    with open(image_path, 'rb') as file:
        image_bytes = file.read()
        
    files = {'file': ('image.jpg', image_bytes)}
    
    response = requests.post(infura_IPFS_url, files=files, auth=(infura_IPFS_api_key, infura_IPFS_api_secret))
    
    if response.status_code == 200:
        ipfs_hash = response.json()['Hash']
        return f'https://ipfs.io/ipfs/{ipfs_hash}'
    else:
        print("Failed to upload to IPFS")

# This function creates the asset and requires the complete metadata template, the URL for your image on IPFS, as well as the asset name and unit as arguments
# This function returns the transaction ID for your asset creation transaction
def create_asset(complete_template, url_for_IPFS, asset_name, asset_unit):

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

    sender_address = 'Your Sender Address Here' # This is the creator of the ARC-69 NFT
    sender_private_key = 'Your Sender Address' Private key in Base64 format' # See get_private_key.py if you do not have your private key in base64 format
    
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
    encoded_tx = encoding.msgpack_encode(signed_asset_creation_tx)
    binary_tx = base64.b64decode(encoded_tx)
    
    submit_tx_endpoint = '/v2/transactions'
    url = node_url + submit_tx_endpoint
    send_transaction = requests.post(url, data=binary_tx)
    response = send_transaction.json()
    return response

#Example Usage
name = 'AshMaker'
description = 'Covered in Ashes and Flaming Hot!'
type = 'Fire'
strength = 5
health = 20
level = 1
exp = 0

#Create a metadata template
complete_template = fill_template(name, description, type, strength, health, level, exp)

#Upload the image to IPFS
image_path = 'ashmaker.jpg'
url_for_IPFS = upload_to_ipfs(image_path)
print(url_for_IPFS)


# Create your asset using your metadata template, URL for image on IPFS, and select your asset_name and asset unit
asset_name = 'AshMaker'
asset_unit = 'PK#1'

transaction_ID = create_asset(complete_template, url_for_IPFS, asset_name, asset_unit)
print(transaction_ID)
