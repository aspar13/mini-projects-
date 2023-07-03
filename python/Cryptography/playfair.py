def prepare_input(text):

    # converting text to uppercase and removing any non-alphabetic characters.
    text = ''.join(filter(str.isalpha, text)).upper()
    return text

def table(key):

	# table for Playfair cipher
	key = prepare_input(key)
	key = key.replace('J','I') # I/J are same 5x5 matrix
	key_table = []

	for char in key:
		if char not in key_table:
			key_table.append(char)

	alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ" 
	for char in alphabet:
		if char not in key_table:
			key_table.append(char)

	key_table = [key_table[i:i+5] for i in range(0,25,5)]
	return key_table

def generate_bigrams(text):

	# generate biagrams and seprate same letters with X
    text = prepare_input(text)

    bigrams = []
    i = 0

    while i < len(text):
        if i == len(text) - 1 or text[i] == text[i + 1]:
            bigrams.append(text[i] + 'X')
            i += 1
        else:
            bigrams.append(text[i] + text[i + 1])
            i += 2
    return bigrams


def find_position(key_table, char):
	# position of a character in the table.
    for row in range(5):
        if char in key_table[row]:
            col = key_table[row].index(char)
            return row, col

def encrypt(bigrams, key_table, encryption = True):

    encrypted_text = ''

    inc = 1
    if encryption == False:
    	inc = -1
    for bigram in bigrams:
        char1, char2 = bigram[0], bigram[1]
        row1, col1 = find_position(key_table, char1)
        row2, col2 = find_position(key_table, char2)
        # the letters are in the same row
        if row1 == row2:
            encrypted_text += key_table[row1][(col1 + inc) % 5] + key_table[row2][(col2 + inc) % 5]
        # the letters are in the same column
        elif col1 == col2:
            encrypted_text += key_table[(row1 + inc) % 5][col1] + key_table[(row2 + inc) % 5][col2]
        # the letters are in a different row and column
        else:
            encrypted_text += key_table[row1][col2] + key_table[row2][col1]

    return encrypted_text

if __name__=='__main__':

	inc = int(input("Press (1) for Encryption (0) for Decryption: "))

	text = input("Enter the text: ")
	key = input("Enter the key: ")

	key_table = table(key)
	bigrams = generate_bigrams(text)

	if inc == 1:
		print ('\n'+'Encripting')
		print (encrypt(bigrams, key_table))
	elif inc == 0:
		print ('\n'+'Decrypting')
		print (encrypt(bigrams, key_table, False))