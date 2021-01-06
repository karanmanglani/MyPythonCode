
def generateKey(string,key):
    if len(string) ==  len(key):
        return key
    else:
        for i in range(len(string) - len(key)):
            key += key[i % len(key)]
        return key

def VignereCipherEncrypt(text,key):
    key = generateKey(text,key)
    cipherText = ''
    ptr = 0
    for char in text:
        cipherText += chr(ord(char) + ord(key[ptr]) % 128)
        ptr += 1
        if ptr == len(key):
            ptr = 0
    return cipherText

def VignereCipherDecrypt(text,key):
    key = generateKey(text,key)
    plainText = ''
    ptr = 0
    for char in text:
        plainText += chr(ord(char) - ord(key[ptr]) + 128 % 128)
        ptr += 1
        if ptr == len(key):
            ptr = 0
    return plainText