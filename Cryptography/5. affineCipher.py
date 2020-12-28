import sys,pyperclip,cryptoMath,random

message = 'Karan is Great'
keyList = [7,3,55]
length = 128
def encryptChar(char,keyList):
    k1,k2,ki = keyList[0],keyList[1],keyList[2]
    return chr((k1 * ord(char) + k2) % length)

def encrypt(message,keyList):
    cipherText = ''
    for i in message:
        cipherText += encryptChar(i,keyList)
    return cipherText

def decryptChar(char,keyList):
    k1,k2,ki = keyList[0],keyList[1],keyList[2]
    return chr(ki * (ord(char) - k2) % length)

def decrypt(cipherText,keyList):
    encryptedText = ''
    for symbol in cipherText:
        encryptedText += decryptChar(symbol,keyList)
    return encryptedText

print(decrypt(encrypt(message , keyList) , keyList)) 
print(encrypt(message,keyList))