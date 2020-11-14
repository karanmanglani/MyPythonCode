
#! KMP String Search Algorithm
str = input("Enter a string: ").lower()
sub = input("Enter string to search in first string: ").lower()

def lps(sub): # lps --> Longest Prefix or pi-table
    i = 0
    j = 1
    m = len(sub)
    lps = [0] * m
    for j in range(1,len(sub)):
        if(sub[j] == sub[i]):
            lps[j] = lps[j - 1] + 1
            i += 1
        else:
            i = 0

    return lps
    
def KMPSearch(str,sub,lps):
    try: 
        j = 0
        for i in range(0,len(str)):        
            if(sub[j] == str[i]):
                j += 1
            else:
                if(lps[j] != 0):
                    j = lps[j - 1] 

            if(j == len(sub)):
                return i - len(sub) + 1 # i - (len(sub) - 1) 

    except IndexError:
        return None

i = KMPSearch(str,sub,lps(sub)) + 1
print("Starting Position = ",i, "\t Ending Position = ", i + len(sub) - 1)
  