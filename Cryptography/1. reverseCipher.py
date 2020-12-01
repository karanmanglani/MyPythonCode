#### Just reverse the given string

message = 'This needs to be Reverse Ciphered'

def encryptor(message):
    i = -len(message)
    encryptedMessage = ''
    for i in range(-1, -len(message) - 1, -1):
        encryptedMessage += message[i]
    return encryptedMessage


def decryptor(message):
    i = -len(message)
    decryptedMessage = ''
    for i in range(-1, -len(message) - 1, -1):
        decryptedMessage += message[i]
    return decryptedMessage

print(encryptor(message))
print(decryptor(encryptor(message)))