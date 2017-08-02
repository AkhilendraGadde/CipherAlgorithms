#!/usr/bin/python3
'''
@ODiN -iwnl-

Requires AdditiveCipher.py , CeaserCipher.py ,
         OneTimePadCipher.py , AutoKeyCipher.py

'''

import AdditiveCipher,CeaserCipher,OneTimePadCipher,AutoKeyCipher

def main():

	while True:
		print('\n\t\t\t||  Cipher Algorithms  ||')
		print('''\n1. Additive Cipher\n2. Ceaser Cipher\n3. One Time Pad Cipher\n4. AutoKey Cipher\n5. Exit\n''')
		ch = int(input('Enter your choice : '))

		if ch is 1:
			AdditiveCipher.additive()
		elif ch is 2:
			CeaserCipher.ceaser()
		elif ch is 3:
			OneTimePadCipher.otpc()
		elif ch is 4:
			AutoKeyCipher.AutoKey()
		elif ch is 5:
			exit(0)
		else:
			print('Invalid Choice')
			pass

# end of main

if __name__ == '__main__':
        main()
