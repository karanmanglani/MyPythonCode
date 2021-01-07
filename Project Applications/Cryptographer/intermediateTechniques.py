### Required helper functions
def generateKey(string,key):
    if len(string) ==  len(key):
        return key
    else:
        for i in range(len(string) - len(key)):
            key += key[i % len(key)]
        return key

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


## Playfair Cipher Encryption

### Base64 Encoding and Decoding
## Base64 Encoding

## Base64 Decoding





