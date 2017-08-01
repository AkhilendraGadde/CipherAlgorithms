'''
@odin
'''
from random import randint as r

def main():

	while True:
		print('\t\t|| Cipher Algorithms ||')
		print('1. Additive Cipher')
		print('2. Ceaser Cipher')
		print('3. One Time Pad Cipher')
		print('4. AutoKey Cipher')
		print('5. Exit')
		ch = int(input('Enter your choice : '))
	
		if ch == 1:
			additive()
		elif ch == 2:
			ceaser()		
		elif ch == 3:
			otpc()
		elif ch == 4:
			AutoKey()
		elif ch == 5:
			exit(0)
		else:
			print('Invalid Choice')
			pass

def additive():
	_charset = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	print('\n\n\t\t|| Additive Cipher ||\n')

	print('\n1. Encrypt Message')
	print('2. Decrypt Message')
	print('3. Return to main')
	ch = int(input('Enter your choice : '))
	
	if ch == 1:
		_cipher = ''
		message = str(input('\nEnter message to encrypt : '))
		key = int(input('Enter key in range[1-26] : '))
		
		for index,i in enumerate(message.replace(" ","")):
			char = _charset.find(i.upper()) + key
			if char > 26:
				char = char%26
			_cipher += _charset[char]
		
		print("\nYour message '{}' is Encrypted as '{}'\n".format(message,_cipher))
		input('press ENTER to continue\n')
	elif ch == 2:
		_cipher = ''
		message = str(input('\nEnter message to decrypt : '))
		key = int(input('Enter key in range[1-26] : '))
		
		for index,i in enumerate(message.upper().replace(" ","")):
			char = _charset.find(i) - key
			if char < 0:
				char += 26
			_cipher += _charset[char].lower()
		
		print("\nYour message '{}' is decrypted as '{}'\n".format(message.upper(),_cipher))
		input('press ENTER to continue\n')
	elif ch == 3:
		pass
	else:
		print('Invalid Choice')
		additive()


def ceaser():
	_charset = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	print('\n\n\t\t|| Ceaser Cipher ||\n')

	print('\n1. Encrypt Message')
	print('2. Decrypt Message')
	print('3. Return to main')
	ch = int(input('Enter your choice : '))
	
	if ch == 1:
		_cipher = ''
		message = str(input('\nEnter message to encrypt : '))
		key = 3
		
		for index,i in enumerate(message.replace(" ","")):
			char = _charset.find(i.upper()) + key
			if char > 26:
				char = char%26
			_cipher += _charset[char]
		
		print("\nYour message '{}' is Encrypted as '{}'\n".format(message,_cipher))
		input('press ENTER to continue\n')
	elif ch == 2:
		_cipher = ''
		message = str(input('\nEnter message to decrypt : '))
		key = 3
		
		for index,i in enumerate(message.upper().replace(" ","")):
			char = _charset.find(i) - key
			if char < 0:
				char += 26
			_cipher += _charset[char].lower()
		
		print("\nYour message '{}' is decrypted as '{}'\n".format(message.upper(),_cipher))
		input('press ENTER to continue\n')
	elif ch == 3:
		pass
	else:
		print('Invalid Choice')
		ceaser()
	
def otpc():
	_charset = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	print('\n\n\t\t|| One Time Pad Cipher ||\n')

	print('\n1. Encrypt Message')
	print('2. Return to main')
	ch = int(input('Enter your choice : '))
	
	if ch == 1:
		_cipher = ''
		message = str(input('\nEnter message to encrypt : '))
		key = r(1,26)
		
		for index,i in enumerate(message.replace(" ","")):
			char = _charset.find(i.upper()) + key
			if char > 26:
				char = char%26
			_cipher += _charset[char]
		
		print("\nYour message '{}' is Encrypted as '{}' using key {}\n".format(message,_cipher,key))
		input('press ENTER to continue\n')
	elif ch == 2:
		pass
	else:
		print('Invalid Choice')
		otpc()
	
def AutoKey():
	_charset = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	print('\n\n\t\t|| AutoKey Cipher ||\n')

	print('\n1. Encrypt Message')
	print('2. Decrypt Message')
	print('3. Return to main')
	ch = int(input('Enter your choice : '))
	
	if ch == 1:
		_cipher = ''
		message = str(input('\nEnter message to encrypt : '))
		key = int(input('Enter key value in range[1-26] : '))
		x = 0
		for index,i in enumerate(message.replace(" ","")):
			char = _charset.find(i.upper()) + key
			if char > 26:
				char = char%26
			_cipher += _charset[char]
		
		print("\nYour message '{}' is Encrypted as '{}'\n".format(message,_cipher))
		input('press ENTER to continue\n')
		
		
		
	elif ch == 2:
		_cipher = ''
		message = str(input('\nEnter message to decrypt : '))
		key = int(input('Enter key in range[1-26] : '))
		
		for index,i in enumerate(message.upper().replace(" ","")):
			char = _charset.find(i) - key
			if char < 0:
				char += 26
			_cipher += _charset[char].lower()
		
		print("\nYour message '{}' is decrypted as '{}'\n".format(message.upper(),_cipher))
		input('press ENTER to continue\n')
	elif ch == 3:
		pass
	else:
		print('Invalid Choice')
		additive()
	

if __name__ == '__main__' :
	main()
	
