
def gcd(a,b):
    while (a > 0 and b > 0):
        if(a >= b):
            a = a % b
        else:
            b = b % a
    return a + b

def lcm(a,b):
    return (a*b) / gcd(a,b)

def betweenTwoSets(a,b):
    multiple = 0
    for i in b:
        multiple = int(gcd(multiple , i))
    
    factor = 1
    for i in a:
        factor = int(lcm(factor,i))
        if(factor > multiple):
            return 0
        
        if(multiple % factor != 0):
            return 0
        
        value = multiple / factor
        maximum = max(factor,value)
        totalX = 1
        for i in range(factor,multiple):
            totalX += 1

        return totalX

print(betweenTwoSets([2,4],[12,24,36])) 