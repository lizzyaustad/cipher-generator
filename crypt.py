def atbash(string):
    alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
            'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    caps = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print ('your string: ', string)
    encrypted = ""
    for letter in string:
        if not letter.isalpha():
            encrypted += letter
        elif letter.islower():
            encrypted += alph[25 - (ord(letter) - 97)]
        else:
            encrypted += caps[25 - caps.index(letter)]
    print ('encrypted string: ', encrypted)


def bacon(string):
    print('your string: ', string)
    to_encrypt = ''
    for letter in string:
        if letter.isalpha():
            to_encrypt += letter

    code = ['aaaaa', 'aaaab', 'aaaba', 'aaabb', 'aabaa', 'aabab', 'aabba',
            'aabbb', 'abaaa', 'abaaa', 'abaab', 'ababa', 'ababb', 'abbaa',
            'abbab', 'abbba', 'abbbb', 'baaaa', 'baaab', 'baaba', 'baabb',
            'baabb', 'babaa', 'babab', 'babba', 'babbb']
    print('your string is ', str(len(to_encrypt)), ' characters')
    prompt = 'please enter plaintext containing ' +\
             str((len(to_encrypt)) * 5) + ' characters: '
    plaintext = input(prompt)
    encrypted = ""
    index = 0
    string.lower()

    for letter in string:
        for char in code[ord(letter) - 97]:
            if char == 'b':
                encrypted += plaintext[index].upper()
                index += 1
            elif char == 'a':
                encrypted += plaintext[index]
                index += 1
            while index < len(plaintext) and not plaintext[index].isalpha():
                encrypted += plaintext[index]
                index += 1
    print ('encrypted string: ', encrypted)


def caesar(string, i):
    print ('your string: ', string)
    encrypted = ""
    for letter in string:
        if not letter.isalpha():
            encrypted += letter
        elif letter.islower():
            num = ord(letter) + i
            if num > 122:
                num = (num - 123) + 97
            elif num < 97:
                num = 123 - (97 - num)
            encrypted += chr(num)
        else:
            num = ord(letter) + i
            if num > 90:
                num = (num - 91) + 65
            elif num < 65:
                num = 91 - (65 - num)
            encrypted += chr(num)

    print ('encrypted string: ', encrypted)


def dna(string):
    print ('your string: ', string)
    code = ['gca', 'b', 'tgc', 'gac', 'gaa', 'ttc', 'gga', 'cac',
            'ata', 'j', 'aaa', 'tta', 'atg', 'aac', 'o', 'cca',
            'caa', 'aga', 'agc', 'aca', 'u', 'gta', 'tgg', 'x',
            'tac', 'z']
    encrypted = ''
    to_encrypt = ''
    for letter in string:
        if letter.isalpha():
            to_encrypt += letter
    to_encrypt.lower()
    for letter in to_encrypt:
        encrypted += code[ord(letter) - 97]
    print ('encrypted string: ', encrypted)


print('~*~*~*~cipher generator~*~*~*~')
string = input('enter string to encrypt: ')
print ('*****************************')
cipher = int(input('1) atbash \n2) bacon \n3)\
caesar \n4) dna \nchoose a cipher: '))
if cipher == 1:
    atbash(string)
elif cipher == 2:
    bacon(string)
elif cipher == 3:
    shift = int(input('enter shift: '))
    caesar(string, shift)
elif cipher == 4:
    dna(string)
else:
    print ('please enter a number from the choices above')
