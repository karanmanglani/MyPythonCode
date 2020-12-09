import pyperclip

def main():
    myMessage = 'Common sense is not so common'
    myKey = 8
    cipherText = encryptMessage(myKey,myMessage)
    print(cipherText + '|')
    pyperclip.copy(cipherText)

def encryptMessage(key,myMessage):
    cipherText = ['']*key
    for col in range(key):
        pointer = col
        while pointer < len(myMessage):
            cipherText[col] += myMessage[pointer]
            pointer += key
    return ''.join(cipherText)

if __name__ == '__main__':
    main()
#### 'Ceno' 'o' '' '' '' '' '' '' 