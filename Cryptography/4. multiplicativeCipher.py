from cryptoMath import modInverse


key = 5
message = 'Karan is a great man'

def multiplicativeCipherEncryption(message,key):
    cipherText = ''
    length = 128
    for i in message:
        index = ord(i)
        encryptedIndex = (index * key) % length
        cipherText += chr(encryptedIndex)
        
    
    return cipherText

def multiplicativeCipherDecryption(cipherText,key):
    decryptedText = ''
    length = 128
    for i in cipherText:
        index = ord(i)
        decryptedIndex = (modInverse(key,length) * index ) % length
        decryptedText += chr(decryptedIndex)
    return decryptedText

print(multiplicativeCipherEncryption(message,key))
print(multiplicativeCipherDecryption(multiplicativeCipherEncryption(message,key),key))