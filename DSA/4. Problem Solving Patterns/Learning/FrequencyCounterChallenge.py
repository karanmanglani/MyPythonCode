################ FREQUENCY COUNTER CHALLENGE ---> ANAGRAM ############

# Function to check if second string is anagram of first string

str1 = input("Enter string 1: ")
str2 = input("Enter string 2: ")

def stringToDictionary(str):
    dict = {}

    for x in str:
        if(x in dict.keys()):
            dict[x] += 1
        else:
            dict[x] = 1

    return dict

def isAnagram(str1 , str2):
    frequencyCounter1 = stringToDictionary(str1)
    frequencyCounter2 = stringToDictionary(str2)
    if(frequencyCounter1 == frequencyCounter2):
        return True
    else:
        return False


print(isAnagram(str1 , str2))