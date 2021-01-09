import base64

plainText = 'karan manglani'.encode('ascii')
encodedText = base64.b64encode(plainText)
decodedText = base64.b64decode(encodedText).decode('ascii')
print('Cipher Text : ' , encodedText)
print('Decoded Text : ' , decodedText)