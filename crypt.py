def caesar(string, i):
	print ('your string: ', string)
	answer = ""
	for letter in string:
		if not letter.isalpha():
			answer += letter
		elif letter.islower():
			num = ord(letter) + i
			if num > 122:
				num = (num-123)+97
			elif num < 97:
				num = 123 - (97-num)
			answer += chr(num)
		else:
			num = ord(letter) + i
			if num > 90:
				num = (num-91)+65
			elif num < 65:
				num = 91 - (65-num)
			answer += chr(num)

	print ('encrypted string: ', answer)

def atbash(string):
	alph = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	caps = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	print ('your string: ', string)
	answer = ""
	for letter in string:
		if not letter.isalpha():
			answer += letter
		elif letter.islower():
			answer += alph[25-(ord(letter)-97)]
		else:
			answer += caps[25-caps.index(letter)]
	print ('encrypted string: ', answer)
	return answer	

print('~*~*~*~Cipher Generator~*~*~*~')
string = input ('Enter string to encrypt: ')
print ('*****************************')
cipher = int(input ('1) Caesar \n2) Atbash \nChoose a cipher: '))
if cipher == 1:
	shift = int(input ('Enter shift: '))
	caesar (string, shift)
elif cipher == 2:
	encrypt = atbash(string)
else:
	print ('Please enter a number')


