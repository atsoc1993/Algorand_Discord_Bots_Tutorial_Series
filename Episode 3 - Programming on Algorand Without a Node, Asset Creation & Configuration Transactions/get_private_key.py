from algosdk import account, mnemonic

#Generate a private key and an algorand address
algorand_private_key, algorand_address = account.generate_account()

#Convert private key to mnemonic phrase to enter into wallet applications like Pera/Defly
mnemonic_phrase = mnemonic.from_private_key(algorand_private_key)

print(algorand_address) # Prints address
print(algorand_private_key) # Prints private key
print(mnemonic_phrase) # Prints mnemonic phrase
