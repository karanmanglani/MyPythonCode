import hashlib
import uuid

### MD5 and SHA Hashes
## MD5 Hasher
def md5Hasher(message):
    return hashlib.md5(message.encode('ascii')).hexdigest()

## SHA 256 hasher
def sha256Hasher(message):
    salt = uuid.uuid4().hex
    return hashlib.sha256(salt.encode() + message.encode('ascii')).hexdigest()

### RSA Algorithm
## RSA Encrypt

## RSA Decrypt