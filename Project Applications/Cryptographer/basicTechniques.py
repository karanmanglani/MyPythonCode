
def reverseCipher(message):
    return message[-1:-len(message) - 1:-1]

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
    
def transpositionCipherEncrypt(message,key):
    return None

def transpositionCipherDecrypt(message,key):
    return None