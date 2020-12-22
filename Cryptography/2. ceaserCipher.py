### Ceaser founded this algorithm
# 
## Following is the basic version algorithm
# Algorithm which can be decrypted iff you know the key
# Take alphabet and replace it with certain distance away from the letter
# for eg if shift is 3, a will become d 
## Now actual algorithm 
# Assign index to each letter then encrypted letter is (index + key) mod (total number of letters)
# To decode decrypted letter is (encryptedIndex - key + total number of letters) mod (total number of letters)

alphabetList = 'abcdefghijklmnopqrstuvwxyz'
print()
key = 2
message = 'karan'

def encryptor(decryptedMessage, key , alphabetList):
    encryptedMessage = ''
    for i in decryptedMessage:
        index = alphabetList.find(i, 0,25)
        if not(index == -1):
            encryptedIndex = (index + key) % len(alphabetList)
            encryptedMessage += alphabetList[encryptedIndex]
    return encryptedMessage

def decryptor(encryptedMessage , key , alphabetList):
    decryptedMessage = ''
    for i in encryptedMessage:
        index = alphabetList.find(i, 0,25)
        if not(index == -1):
            decryptedIndex = (index + len(alphabetList) - key) % len(alphabetList)
            decryptedMessage += alphabetList[decryptedIndex]
    return decryptedMessage

print(decryptor(encryptor(message, key , alphabetList),key,alphabetList))
print(encryptor(message, key , alphabetList))

## Disadvantage :- Can be breaken by bruteforce attack

def bruteforce(encryptedMessage, alphabetList):
    possibleMessage = []
    for i in range(len(alphabetList) + 1):
        possibleMessage.append(decryptor(encryptedMessage, i, alphabetList))
    return possibleMessage

for i in bruteforce(encryptor(message, key,alphabetList), alphabetList):
    print(i) 