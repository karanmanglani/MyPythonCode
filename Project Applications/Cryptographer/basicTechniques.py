import math

#### Reverse Cipher
def reverseCipher(message):
    return message[-1:-len(message) - 1:-1]

### Ceaser Cipher
## Ceaser Cipher Encrypt
def ceaserCipherEncrypt(decryptedMessage,key,alphabetList):
    try:
        encryptedMessage = ''
        for i in decryptedMessage:
            index = alphabetList.find(i, 0,25)
            if not(index == -1):
                encryptedIndex = (index + key) % len(alphabetList)
                encryptedMessage += alphabetList[encryptedIndex]
        return encryptedMessage
    except:
        return None

## Ceaser Cipher Decrypt
def ceaserCipherDecrypt(encryptedMessage,key,alphabetList):
    try:
        decryptedMessage = ''
        for i in encryptedMessage:
            index = alphabetList.find(i, 0,25)
            if not(index == -1):
                decryptedIndex = (index + len(alphabetList) - key) % len(alphabetList)
                decryptedMessage += alphabetList[decryptedIndex]
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

## Multiplicative Cipher Decrypt