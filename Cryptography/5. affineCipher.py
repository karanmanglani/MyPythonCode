import sys,pyperclip,cryptoMath,random

message = 'Karan is Great'
keyList = [3,20]
length = 128

def encrypt(message,key):
    global length
    encryptedMessage = ''
    for i in message:
        index = ord(i)
        encryptedIndex = ((key[0] * index) + key[1]) % length
        encryptedMessage += chr(encryptedIndex)
    return encryptedMessage

def decrypt(message,key):
    global length
    decryptedMessage = ''
    for i in message:
        index = ord(i)
        decryptedIndex = (cryptoMath.modInverse(key[0],length)*(index - key[1])) % length
        decryptedMessage += chr(decryptedIndex)
    return decryptedMessage

print(decrypt(encrypt(message , keyList) , keyList)) 
print(encrypt(message,keyList))