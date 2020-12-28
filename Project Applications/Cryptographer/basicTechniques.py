import math

### Maths for Cryptography
def gcd(a,b):
    while a!= 0:
        a,b = b%a,a
    return b

def modInverse(a,m):
    a = a % m
    for i in range(1,m):
        if((a*i) % m == 1):
            return i
    return 1

#### Reverse Cipher
def reverseCipher(message):
    return message[-1:-len(message) - 1:-1]

### Ceaser Cipher
## Ceaser Cipher Encrypt
def ceaserCipherEncrypt(decryptedMessage,key):
    try:
        encryptedMessage = ''
        for i in decryptedMessage:
            index = ord(i)
            if not(index == -1):
                encryptedIndex = (index + key) % 128
                encryptedMessage += chr(encryptedIndex)
        return encryptedMessage
    except:
        return None

## Ceaser Cipher Decrypt
def ceaserCipherDecrypt(encryptedMessage,key):
    try:
        decryptedMessage = ''
        for i in encryptedMessage:
            index = ord(i)
            if not(index == -1):
                decryptedIndex = (index + 128 - key) % 128
                decryptedMessage += chr(decryptedIndex)
        return decryptedMessage
    except:
        return None

### Transposition Cipher
## Transposition Cipher Encrypt
def transpositionCipherEncrypt(message,key):
    cipherText = ['']*key
    for col in range(key):
        pointer = col
        while pointer < len(message):
            cipherText[col] += message[pointer]
            pointer += key
    return ''.join(cipherText)

## Transposition Cipher Decrypt
def transpositionCipherDecrypt(message,key):
    numberOfColumns = math.ceil(len(message) / key)
    numberOfRows = key
    shadedBoxes = (numberOfColumns * numberOfRows) - len(message)
    plainText = [''] * numberOfColumns
    col = 0
    row = 0

    for character in message:
        plainText[col] += character
        col += 1
        if(col == numberOfColumns or (col == numberOfColumns - 1 and row >= numberOfRows- shadedBoxes)):
            col = 0
            row += 1
        
    return ''.join(plainText)

### Multipicative Cipher
## Multiplicative cipher Encrypt
def multiplicativeCipherEncrypt(message,key):
    encryptedMessage = ''
    length = 128
    if(gcd(key,length) == 1):
        for i in message:
            index = ord(i)
            encryptedIndex = (index * key) % length
            encryptedMessage += chr(encryptedIndex)
        return encryptedMessage
    else:
        return 'Please Chose a key such that gcd of key and 128 is 1'
## Multiplicative Cipher Decrypt
def multiplicativeCipherDecrypt(message,key):
    decryptedMessage = ''
    length = 128
    if(gcd(key,length) == 1):
        for i in message:
            index = ord(i)
            decryptedIndex = (modInverse(key,length) * index ) % length
            decryptedMessage += chr(decryptedIndex)
        return decryptedMessage
    else:
        return 'Please Chose a key such that gcd of key and 128 is 1'



### Affine Cipher
## Affine Cipher Encryption
def affineCipherEncrypt(message,keyList):
    length = 128
    encryptedMessage = ''
    if(gcd(keyList[0] , length) == 1):
        for i in message:
            index = ord(i)
            encryptedIndex = (index * keyList[0] + keyList[1]) % length
            encryptedMessage += chr(encryptedIndex)
        return encryptedMessage
    else:
        return 'Please Chose multiply key such that gcd of key and 128 is 1'
## Affine Cipher Decryption
def affineCipherDecrypt(message,keyList):
    length = 128
    decryptedMessage = ''
    if(gcd(keyList[0] , length) == 1):
        for i in message:
            index = ord(i)
            decryptedIndex = modInverse(keyList[0],length) * (index - keyList[1]) % length
            decryptedMessage += chr(decryptedIndex)
        return decryptedMessage
    else:
        return 'Please Chose multiply key such that gcd of key and 128 is 1'



### Substitution Cipher
## Substitution Cipher Encryption

## Substitution Cipher Decryption

