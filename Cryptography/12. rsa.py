import cryptoMath

def keyMaker(p,q,k):
    #Checking  if inputs are prime
    if cryptoMath.gcd(p,q) != 1:
        return None
    rsaModulus = p*q
    euilersToitent = (p-1)  * (q - 1)
    e = 1
    for i in range(euilersToitent - 1, 1, -1):
        if cryptoMath.gcd(i , rsaModulus) == 1 : 
            e = i
            break
    # Public Key = rsaModulus and e
    d = (k * euilersToitent + 1) // e
    return [[e,rsaModulus],[d,rsaModulus]]

def rsaEncrypt(p,q,k,message):
    publicKey  = keyMaker(p,q,k)[0]
    e,n = publicKey
    x = []
    for i in message:
        if(i.isupper()):
            m = ord(i)-65
            c=(m**e)%n
            x.append(c)
        elif(i.islower()):               
            m= ord(i)-97
            c=(m**e)%n
            x.append(c)
    return x

def rsaDecrypt(p,q,k,cText):
    privateKey = keyMaker(p,q,k)[1]
    d,n = privateKey
    x = ''
    m = 0
    for i in cText:
        m=(int(i)**d)%n
        m+=65
        c=chr(m)
        x+=c
    return x

print(rsaEncrypt(53,59,2,'karan'))
print(rsaDecrypt(53,59,2,rsaEncrypt(53,9,2,'karan')))


### NOT Complete