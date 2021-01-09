import string
import hashlib
import uuid

alphabets = string.ascii_lowercase
### Required helper functions
def generateKey(string,key):
    if len(string) ==  len(key):
        return key
    else:
        for i in range(len(string) - len(key)):
            key += key[i % len(key)]
        return key

def generateKeyPF(key,usedCharacters):
    global alphabets
    keyString = ''
    keyList = []
    for i in key:
        if i not in usedCharacters:
            keyString += i
            usedCharacters += i
    if len(keyString) != 25:
        for i in range(26):
            if alphabets[i] not in usedCharacters and len(keyString) != 25:
                keyString += alphabets[i]
                usedCharacters += alphabets[i]

    for i in range(5):
        keyList.append(keyString[i * 5: i*5 + 5])
    return keyList

def plainTextPairCreater(message):
    textList = []
    for i in range(0,len(message),2):
        a = message[i]
        if i+1 == len(message) or message[i] == message[i+1]:
            b = 'x'
        else:
            b = message[i+1]
        textList.append(a+b)
    return textList

def cipherTextPairCreater(cipherText):
    textList = []
    for i in range(0,len(cipherText),2):
        b= cipherText[i+1]
        a = cipherText[i]
        if b == 'x':
            if i+1 == len(cipherText):
                b = ''
            else:
                b = a
        textList.append(a+b)
    return textList

### Vernam Cipher
## Vernam Cipher Encryption
def vernamCipherEncrypt(text,key):
    cipherText = ''
    ptr = 0
    for char in text:
        cipherText += chr(ord(char) + ord(key[ptr]) % 128)
        ptr += 1
        if ptr == len(key):
            ptr = 0
    return cipherText
## Vernam Cipher Decryption
def vernamCipherDecrypt(text,key):
    plainText = ''
    ptr = 0
    for char in text:
        plainText += chr(ord(char) - ord(key[ptr]) + 128 % 128)
        ptr += 1
        if ptr == len(key):
            ptr = 0
    return plainText

### Vignere Cipher 
## Vignere Cipher Encrytion
def vignereCipherEncrypt(text,key):
    key = generateKey(text,key)
    cipherText = ''
    ptr = 0
    for char in text:
        cipherText += chr(ord(char) + ord(key[ptr]) % 128)
        ptr += 1
        if ptr == len(key):
            ptr = 0
    return cipherText

## Vignere Cipher Decryption
def vignereCipherDecrypt(text,key):
    key = generateKey(text,key)
    plainText = ''
    ptr = 0
    for char in text:
        plainText += chr(ord(char) - ord(key[ptr]) + 128 % 128)
        ptr += 1
        if ptr == len(key):
            ptr = 0
    return plainText

### Playfaire Cipher
## Playfaire Cipher Encryption
def playfairCipherEncrypt(key,message,toRemove):
    keyMatrix = generateKeyPF(key,toRemove)
    plainTextPairs = plainTextPairCreater(message)
    cipherText = ''
    for pair in plainTextPairs:
        appliedRule = False
        for row in keyMatrix:
            if pair[0] in row and pair[1] in row:
                j0 = row.find(pair[0])
                j1 = row.find(pair[1])
                cipherText += row[(j0 + 1) % 5] + row[(j1 + 1) % 5]
                appliedRule = True
            
        if not appliedRule:
            for j in range(5):
                col = ''.join(keyMatrix[i][j] for i in range(5))
                if pair[0] in col and pair[1] in col:
                    j0 = col.find(pair[0])
                    j1 = col.find(pair[1])
                    cipherText += col[(j0 + 1) % 5] + col[(j1 + 1) % 5]
                    appliedRule = True
                    
        if not appliedRule:
            i0 = 0
            j0 = 0
            i1 = 0
            j1 = 0
            for i in range(5):
                row = keyMatrix[i]
                if pair[0] in row:
                    i0 = i
                    j0 = row.find(pair[0])
                
                if pair[1] in row:
                    i1 = i
                    j1 = row.find(pair[1])
            cipherText += keyMatrix[i0][j1] + keyMatrix[i1][j0]
    return cipherText

## Playfair Cipher Decryption
def playfairCipherDecrypt(key,message,toRemove):
    keyMatrix = generateKeyPF(key,toRemove)
    cipherTextPairs = cipherTextPairCreater(message)
    plainText = ''
    for pair in cipherTextPairs:
        appliedRule = False
        for row in keyMatrix:
            if pair[0] in row and pair[1] in row:
                j0 = row.find(pair[0])
                j1 = row.find(pair[1])
                plainText += row[(j0 + 4) % 5] + row[(j1 + 4) % 5]
                appliedRule = True
            
        if not appliedRule:
            for j in range(5):
                col = ''.join(keyMatrix[i][j] for i in range(5))
                if pair[0] in col and pair[1] in col:
                    j0 = col.find(pair[0])
                    j1 = col.find(pair[1])
                    plainText += col[(j0 + 4) % 5] + col[(j1 + 4) % 5]
                    appliedRule = True
                    
        if not appliedRule:
            i0 = 0
            j0 = 0
            i1 = 0
            j1 = 0
            for i in range(5):
                row = keyMatrix[i]
                if pair[0] in row:
                    i0 = i
                    j0 = row.find(pair[0])
                
                if pair[1] in row:
                    i1 = i
                    j1 = row.find(pair[1])
            plainText += keyMatrix[i0][j1] + keyMatrix[i1][j0]
    return plainText

### Base64 Encoding and Decoding
## Base64 Encoding

## Base64 Decoding
