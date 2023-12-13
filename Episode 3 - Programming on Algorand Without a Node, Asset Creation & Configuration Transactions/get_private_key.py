from algosdk import account, mnemonic

#Generate a private key and an algorand address
algorand_private_key, algorand_address = account.generate_account()

#Convert private key to mnemonic phrase to enter into wallet applications like Pera/Defly
mnemonic_phrase = mnemonic.from_private_key(algorand_private_key)

#Convert mnemonic phrase to private key
#A mnemonic phrase is 25 words long
mnemonic_phrase_example = "one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen twenty twentyone twentytwo twentythree twentyfour twentyfive"
private_key_from_mnemonic = mnemonic.to_private_key(mnemonic_phrase_example)

print(private_key_from_mnemonic) # Prints private key obtained from mnemonic phrase
print(algorand_address) # Prints address
print(algorand_private_key) # Prints private key
print(mnemonic_phrase) # Prints mnemonic phrase
