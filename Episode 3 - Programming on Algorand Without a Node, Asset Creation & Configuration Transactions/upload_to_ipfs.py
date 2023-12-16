import requests
import json

infura_IPFS_api_key = 'INFURA API KEY HERE'
infura_IPFS_api_secret = 'INFURA API SECRET HERE'
infura_IPFS_url = 'https://ipfs.infura.io:5001/api/v0/add'

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
      
# Path to the image in this folder
image_path = 'ashmaker.jpg' 

# Call upload_to_ipfs function with image_path argument, returns the URL to IPFS where image is hosted
url_for_IPFS = upload_to_ipfs(image_path) 

# Prints the URL generated
print(url_for_IPFS)
