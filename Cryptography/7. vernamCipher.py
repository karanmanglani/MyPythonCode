
def makeVernamCipher(text,key):
    result = ''
    ptr = 0
    for char in text:
        result += chr(ord(char) ^ ord(key[ptr]))
        ptr += 1
        if ptr == len(key):
            ptr = 0
    return result

print(makeVernamCipher('karan','@$cd1'))
print(makeVernamCipher(makeVernamCipher('karan','@$cd1'),'@$cd1'))