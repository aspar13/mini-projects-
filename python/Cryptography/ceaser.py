def caesar(key, message):
    cypher_text = ""
    for char in message:
        if char.isalpha():
            if char.isupper():
                cypher_text += chr((ord(char) - 65 + key) % 26 + 65)
            else:
                cypher_text += chr((ord(char) - 97 + key) % 26 + 97)
        else:
            cypher_text += char
    return cypher_text

if __name__ == '__main__':

	inc = int(input("Press (1) for Encryption (0) for Decryption: "))

	text = input("Enter text message: ")
	key = int(input("Enter the key: "))

	if inc == 1:
		print('\n'+'encrypted message:')
		encoded = caesar(key, text)
		print(encoded)

	elif inc == 0:
	    print('\n'+'decrypted message:')
	    decoded = caesar(-key, text)
	    print(decoded)