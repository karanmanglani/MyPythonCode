import sys,pyperclip,random

letters = 'abcdefghijklmnopqrstuvwxyz'
letters  += letters.upper()
key = 'bacfedhgiljkomnrpqustxvwzy'
key += key.upper()
print(letters)
print(key)

def encrypt(letters,message,key):
    encryptedMessage = ''
    if len(letters) != len(key):
        return 'Lenth of key and letter is not same'
    for i in message:
        if i in letters:
            index = letters.find(i)
            encryptedMessage += key[index]
        else:
            encryptedMessage += i
    return encryptedMessage

def decrypt(letters,message,key):
    decryptedMessage = ''
    if len(letters) != len(key):
        return 'Lenth of key and letter is not same'
    
    for i in message:
        if i in key:
            index = key.find(i)
            decryptedMessage += letters[index]
        else:
            decryptedMessage += i
    return decryptedMessage

print(decrypt(letters,'Jbqbm iu hqebs',key))
