import hashlib
import uuid

hashValue = hashlib.md5('karan manglani'.encode('ascii'))
print(hashValue.hexdigest())

## password check using md5
def hashPassword(password):
    salt = uuid.uuid4().hex
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt

def checkPassword(hashedPassword,userPassword):
    password , salt = hashedPassword.split(':')
    return password == hashlib.sha256(salt.encode() + userPassword.encode()).hexdigest()

newPassword = input("Please enter a password: ")
hashedPassword = hashPassword(newPassword)
print('string in db: '+hashedPassword)
oldPassword = input('Enter the password again : ')
if checkPassword(hashedPassword,oldPassword):
    print('You entered right password ')
else:
    print('You entered a wrong password')