#!/usr/bin/python3
'''
@odin
'''

from random import randint as ri

_charset = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def otpc():

	_plainText = ''
	_cipherText = ''
	key = ri(1,26)

	print('\n\n\t\t|| OneTimePad Cipher ||\n')
	print('''\n1. Encrypt Message\n2. Return to main\n''')
	ch = int(input('Enter your choice : '))

	if ch is 1:
		_cipherText = ''
		_plainText = str(input('\nEnter message to encrypt : ')).upper().replace(" ","")

		for index,i in enumerate(_plainText):
			char = _charset.find(i) + key
			if char > 26:
				char = char%26
			_cipherText += _charset[char]

		print("\nYour message '{}' is Encrypted as '{}' using key {}\n".format(_plainText.lower(),_cipherText,key))
		input('press ENTER to continue\n')
		otpc()

	elif ch is 2:
		pass
	else:
		print('Invalid Choice')
		otpc()

if __name__ == '__otpc__' :
	otpc()
