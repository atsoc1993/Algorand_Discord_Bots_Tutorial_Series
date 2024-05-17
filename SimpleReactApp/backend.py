
import requests
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/return_block_info', methods=['GET'])
def get_block_and_transaction_ids():
    print("Running function")
    status_endpoint = 'https://mainnet-api.algonode.cloud/v2/status'
    response = requests.get(status_endpoint)
    last_block = response.json()['last-round']
  
    block_info_url = 'https://mainnet-idx.algonode.cloud/v2/blocks/'
    complete_url = block_info_url + str(last_block) 
    response = requests.get(complete_url)
  
    transaction_info = response.json().get('transactions', [])
    block_info = {last_block: []}
    
    if transaction_info != []:

        for t in transaction_info:
            transaction_id = t.get('id', "")
            block_info[last_block].append(transaction_id)
          
    return jsonify({"message": block_info})
            
if __name__ == '__main__':
    app.run(debug=True)
