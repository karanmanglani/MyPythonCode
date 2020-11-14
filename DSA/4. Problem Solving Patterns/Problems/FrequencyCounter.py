str = input("Enter a passage: ").upper().split(" ")

def countWordsFrequency(str):
    frequencyCounter = {}
    for word in str:
        if(word in frequencyCounter):
            frequencyCounter[word] += 1
        else:
            frequencyCounter[word] = 1
    return frequencyCounter

print(countWordsFrequency(str))