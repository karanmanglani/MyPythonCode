def gcd(a,b):
    while a != 0:
        a,b = b%a,a
    return b


def modInverse(a,m):
    a = a % m
    for x in range(1,m):
        if((a * x) % m == 1):
            return x
    return 1 

