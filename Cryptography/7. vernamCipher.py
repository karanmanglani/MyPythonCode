


def VernamCipherEncrypt(text,key):
    cipherText = ''
    ptr = 0
    for char in text:
        cipherText += chr(ord(char) + ord(key[ptr]) % 128)
        ptr += 1
        if ptr == len(key):
            ptr = 0
    return cipherText

def VernamCipherDecrypt(text,key):
    plainText = ''
    ptr = 0
    for char in text:
        plainText += chr(ord(char) - ord(key[ptr]) + 128 % 128)
        ptr += 1
        if ptr == len(key):
            ptr = 0
    return plainText

print(VernamCipherEncrypt('karan','@$#23'))
print(VernamCipherDecrypt(VernamCipherEncrypt('karan','@$#23'),'@$#23'))
