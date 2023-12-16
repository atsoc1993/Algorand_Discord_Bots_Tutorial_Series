import requests
from algosdk.v2client import *
from algosdk.transaction import AssetCreateTxn
import json

algod_token = '9225f0a6a3bb74686ed65bc16e06705df9f39a704b77f3c5c6950ca3051431eb'
algod_port = 'http://127.0.0.1:8080'
infura_IPFS_api_key = '2Td1fh2USAAxUxPTSHW7wjTszNv'
infura_IPFS_api_secret = '468f3a6422ab26a6f05bffd4ab73dc30'
infura_IPFS_url = 'https://ipfs.infura.io:5001/api/v0/add'


def create_template():
    return {
        "standard": "arc69",
        "mime_type": "image/jpg",
        "properties": {}
    }

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




def create_asset(complete_template, url_for_IPFS, asset_name, asset_unit):
    algod_client = algod.AlgodClient(algod_token, algod_port)
    sender_address = '355DZGHWORZRHM66NOJXOPG5OMD6NUJWFYLG5UDGBUVSCBH25PJ4BVEHJI'
    sender_private_key = '1KcfFjzsHriFRo2CR//RV1xIUFDKT9k3fl5pATEZGtXfejyY9nRzE7Pea5N3PN1zB+bRNi4WbtBmDSshBPrr0w=='
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


name = 'AshMaker'
description = 'Covered in Ashes and Flaming Hot!'
type = 'Fire'
strength = 5
health = 20
level = 1
exp = 0

complete_template = fill_template(name, description, type, strength, health, level, exp)


image_path = 'ashmaker.jpg'
url_for_IPFS = upload_to_ipfs(image_path)
print(url_for_IPFS)

asset_name = 'AshMaker'
asset_unit = 'PK#1'

transaction_ID = create_asset(complete_template, url_for_IPFS, asset_name, asset_unit)
print(transaction_ID)

