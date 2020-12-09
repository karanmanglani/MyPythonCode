import pyperclip,math

def main():
    myMessage = 'Common sense is not so common'
    myKey = 8
    cipherText = encryptMessage(myKey,myMessage)
    print(cipherText + '|')
    pyperclip.copy(cipherText)
    plainText = decryptMessage(myKey, cipherText)
    print(plainText )
    pyperclip.copy(plainText)

def encryptMessage(key,myMessage):
    cipherText = ['']*key
    for col in range(key):
        pointer = col
        while pointer < len(myMessage):
            cipherText[col] += myMessage[pointer]
            pointer += key
    return ''.join(cipherText)

def decryptMessage(key,encryptedMessage):
    numberOfColumns = math.ceil(len(encryptedMessage) / key)
    numberOfRows = key
    shadedBoxes = (numberOfColumns * numberOfRows) - len(encryptedMessage)
    plainText = [''] * numberOfColumns
    col = 0
    row = 0

    for character in encryptedMessage:
        plainText[col] += character
        col += 1
        if(col == numberOfColumns or (col == numberOfColumns - 1 and row >= numberOfRows- shadedBoxes)):
            col = 0
            row += 1
        
    return ''.join(plainText)

if __name__ == '__main__':
    main()
#### 'Ceno' 'o' '' '' '' '' '' '' 