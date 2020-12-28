### Ceaser founded this algorithm
# 
## Following is the basic version algorithm
# Algorithm which can be decrypted iff you know the key
# Take alphabet and replace it with certain distance away from the letter
# for eg if shift is 3, a will become d 
## Now actual algorithm 
# Assign index to each letter then encrypted letter is (index + key) mod (total number of letters)
# To decode decrypted letter is (encryptedIndex - key + total number of letters) mod (total number of letters)

key = 2
message = 'karan'

def encryptor(decryptedMessage, key):
    encryptedMessage = ''
    for i in decryptedMessage:
        index = ord(i)
        if not(index == -1):
            encryptedIndex = (index + key) % 128
            encryptedMessage += chr(encryptedIndex)
    return encryptedMessage

def decryptor(encryptedMessage , key):
    decryptedMessage = ''
    for i in encryptedMessage:
        index = ord(i)
        if not(index == -1):
            decryptedIndex = (index + 128 - key) % 128
            decryptedMessage += chr(decryptedIndex)
    return decryptedMessage

print(decryptor(encryptor(message, key , ),key,))
print(encryptor(message, key , ))

## Disadvantage :- Can be breaken by bruteforce attack

def bruteforce(encryptedMessage, alphabetList):
    possibleMessage = []
    for i in range(129):
        possibleMessage.append(decryptor(encryptedMessage, i))
    return possibleMessage

for i in bruteforce(encryptor(message, key),key):
    print(i) 