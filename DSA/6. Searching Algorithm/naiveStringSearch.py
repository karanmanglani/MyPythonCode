str = input("Enter a string: ").lower()
sub = input("Enter string to search in first string: ").lower()

def stringSearch(str,sub):
    count = 0
    for i in range(0,len(str)):
        for j in range(0,len(sub)):
            if(sub[j] !=  str[i + j]):
                break
            if(j == len(sub) - 1):
                count += 1
    
    return count

print(stringSearch(str,sub))