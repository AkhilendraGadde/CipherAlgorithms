#!/usr/bin/python3
'''
@odin
'''

_charset = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def AutoKey():

	_plainText = ''
	_cipherText = ''

	print('\n\n\t\t|| AutoKey Cipher ||\n')
	print('''\n1. Encrypt Message\n2. Decrypt Message\n3. Return to main\n''')
	ch = int(input('Enter your choice : '))

	if ch is 1:
		_cipherText = ''
		_plainText = str(input('\nEnter message to encrypt : ')).upper().replace(" ","")
		key = int(input('Enter key in range[1-26] : '))

		for index,i in enumerate(_plainText):
			if index is 0:
				char = _charset.find(i) + key
			else:
				char = _charset.find(i) + _charset.find(_plainText[index - 1])
				if char > 26:
					char %= 26
			_cipherText += _charset[char]

		print("\nYour message '{}' is Encrypted as '{}'\n".format(_plainText.lower(),_cipherText))
		input('press ENTER to continue\n')
		AutoKey()

	# Decryption main logic by keyser soze! Hail PappA
	elif ch is 2:
		_plainText = ''
		_cipherText = str(input('\nEnter message to decrypt : ')).upper().replace(" ","")
		key = int(input('Enter key in range[1-26] : '))

		for index,i in enumerate(_cipherText):
			if index is 0:
				char = _charset.find(i) - key
			else:
				char = _charset.find(i) - _charset.find(_plainText[index - 1])
				if char < 0:
					char += 26
			print(char)
			_plainText += _charset[char]
		print("\nYour message '{}' is decrypted as '{}'\n".format(_cipherText,_plainText.lower()))
		input('press ENTER to continue\n')
		AutoKey()

	elif ch is 3:
		pass

	else:
		print('Invalid Choice')
		AutoKey()


if __name__ == '__AutoKey__' :
	AutoKey()
