#!/usr/bin/python3
'''
@odin
'''

from random import randint as ri
_charset = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main():

	while True:
		print('\n\t\t\t||  Cipher Algorithms  ||')
		print('''\n1. Additive Cipher\n2. Ceaser Cipher\n3. One Time Pad Cipher\n4. AutoKey Cipher\n5. Exit\n''')
		ch = int(input('Enter your choice : '))

		if ch is 1:
			additive()
		elif ch is 2:
			ceaser()
		elif ch is 3:
			otpc()
		elif ch is 4:
			AutoKey()
		elif ch is 5:
			exit(0)
		else:
			print('Invalid Choice')
			pass

# end of main

def additive():

	_plainText = ''
	_cipherText = ''

	print('\n\n\t\t|| Additive Cipher ||\n')
	print('''\n1. Encrypt Message\n2. Decrypt Message\n3. Return to main\n''')
	ch = int(input('Enter your choice : '))

	if ch is 1:
		_cipherText = ''
		_plainText = str(input('\nEnter message to encrypt : ')).upper().replace(" ","")
		key = int(input('Enter key in range[0-25] : '))
		if key>25 and key < 0:
			print("Invalid key value")
			additive()

		for index,i in enumerate(_plainText):
			char = _charset.find(i) + key
			if char > 25:
				char = char%26
			_cipherText += _charset[char]

		print("\nYour message '{}' is Encrypted as '{}'\n".format(_plainText.lower(),_cipherText))
		input('press ENTER to continue\n')
		additive()

	elif ch is 2:
		_plainText = ''
		_cipherText = str(input('\nEnter message to decrypt : ')).upper().replace(" ","")
		key = int(input('Enter key in range[0-25] : '))
		if key>25 and key < 0:
			print("Invalid key value")
			additive()

		for index,i in enumerate(_cipherText):
			char = _charset.find(i) - key
			if char < 0:
				char += 26
			_plainText += _charset[char]

		print("\nYour message '{}' is decrypted as '{}'\n".format(_cipherText,_plainText.lower()))
		input('press ENTER to continue\n')
		additive()

	elif ch is 3:
		pass
	else:
		print('Invalid Choice')
		additive()


def ceaser():

	_plainText = ''
	_cipherText = ''
	key = 3

	print('\n\n\t\t|| Ceaser Cipher ||\n')
	print('''\n1. Encrypt Message\n2. Decrypt Message\n3. Return to main\n''')
	ch = int(input('Enter your choice : '))

	if ch is 1:
		_cipherText = ''
		_plainText = str(input('\nEnter message to encrypt : ')).upper().replace(" ","")

		for index,i in enumerate(_plainText):
			char = _charset.find(i) + key
			if char > 25:
				char = char%26
			_cipherText += _charset[char]

		print("\nYour message '{}' is Encrypted as '{}'\n".format(_plainText.lower(),_cipherText))
		input('press ENTER to continue\n')
		ceaser()

	elif ch is 2:
		_plainText = ''
		_cipherText = str(input('\nEnter message to decrypt : ')).upper().replace(" ","")

		for index,i in enumerate(_cipherText):
			char = _charset.find(i) - key
			if char < 0:
				char += 26
			_plainText += _charset[char]

		print("\nYour message '{}' is decrypted as '{}'\n".format(_cipherText,_plainText.lower()))
		input('press ENTER to continue\n')
		ceaser()

	elif ch is 3:
		pass
	else:
		print('Invalid Choice')
		ceaser()


def otpc():

	_plainText = ''
	_cipherText = ''
	key = ''

	print('\n\n\t\t|| OneTimePad Cipher ||\n')
	print('''\n1. Encrypt Message\n2. Return to main\n''')
	ch = int(input('Enter your choice : '))

	if ch is 1:
		_cipherText = ''
		_plainText = str(input('\nEnter message to encrypt : ')).upper().replace(" ","")

		for char in range(len(_plainText)):
			key += _charset[ri(0,25)]

		for index,i in enumerate(_plainText):
			char = _charset.find(i) + _charset.find(key[index])
			if char > 25:
				char -= 26
			_cipherText += _charset[char]

		print("\nYour message '{}' is Encrypted as '{}' using key {}\n".format(_plainText.lower(),_cipherText,key))
		input('press ENTER to continue\n')
		otpc()

	elif ch is 2:
		pass
	else:
		print('Invalid Choice')
		otpc()


def AutoKey():

	_plainText = ''
	_cipherText = ''

	print('\n\n\t\t|| AutoKey Cipher ||\n')
	print('''\n1. Encrypt Message\n2. Decrypt Message\n3. Return to main\n''')
	ch = int(input('Enter your choice : '))

	if ch is 1:
		_cipherText = ''
		_plainText = str(input('\nEnter message to encrypt : ')).upper().replace(" ","")
		key = int(input('Enter key in range[0-25] : '))
		if key>25 and key < 0:
			print("Invalid key value")
			AutoKey()

		for index,i in enumerate(_plainText):
			if index is 0:
				char = _charset.find(i) + key
			else:
				char = _charset.find(i) + _charset.find(_plainText[index - 1])
				if char > 25:
					char %= 26
			_cipherText += _charset[char]

		print("\nYour message '{}' is Encrypted as '{}'\n".format(_plainText.lower(),_cipherText))
		input('press ENTER to continue\n')
		AutoKey()

	# Decryption main logic by keyser soze! Hail PappA
	elif ch is 2:
		_plainText = ''
		_cipherText = str(input('\nEnter message to decrypt : ')).upper().replace(" ","")
		key = int(input('Enter key in range[0-25] : '))
		if key>25 and key < 0:
			print("Invalid key value")
			AutoKey()
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


# Avoid exection of complete module while importing into other script
if __name__ == '__main__' :
	main()
