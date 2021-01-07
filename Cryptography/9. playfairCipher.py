import string
alphabets = string.ascii_lowercase

def generateKey(key):
    global alphabets
    usedCharacters = 'j'
    keyString = ''
    keyList = []
    for i in key:
        if i not in usedCharacters:
            keyString += i
            usedCharacters += i
    if len(keyString) != 25:
        for i in range(26):
            if alphabets[i] not in usedCharacters and len(keyString) != 25:
                keyString += alphabets[i]
                usedCharacters += alphabets[i]

    for i in range(5):
        keyList.append(keyString[i * 5: i*5 + 5])
    return keyList

def pairCreater(message):
    
    textList = []
    for i in range(0,len(message),2):
        a = message[i]
        if i+1 == len(message) or message[i] == message[i+1]:
            b = 'x'
        else:
            b = message[i+1]
        textList.append(a+b)
    return textList


def playfairCipherEncrypt(key,message):
    keyMatrix = generateKey(key)
    plainTextPairs = pairCreater(message)
    cipherText = ''
    for pair in plainTextPairs:
        appliedRule = False
        for row in keyMatrix:
            if pair[0] in row and pair[1] in row:
                j0 = row.find(pair[0])
                j1 = row.find(pair[1])
                cipherText += row[(j0 + 1) % 5] + row[(j1 + 1) % 5]
                appliedRule = True
            
        if not appliedRule:
            for j in range(5):
                col = ''.join(keyMatrix[i][j] for i in range(5))
                if pair[0] in col and pair[1] in col:
                    j0 = col.find(pair[0])
                    j1 = col.find(pair[1])
                    cipherText += col[(j0 + 1) % 5] + col[(j1 + 1) % 5]
                    appliedRule = True
                    
        if not appliedRule:
            i0 = 0
            j0 = 0
            i1 = 0
            j1 = 0
            for i in range(5):
                row = keyMatrix[i]
                if pair[0] in row:
                    i0 = i
                    j0 = row.find(pair[0])
                
                if pair[1] in row:
                    i1 = i
                    j1 = row.find(pair[1])
            cipherText += keyMatrix[i0][j1] + keyMatrix[i1][j0]
    return cipherText

print(playfairCipherEncrypt('karan','karanisgreat'))
