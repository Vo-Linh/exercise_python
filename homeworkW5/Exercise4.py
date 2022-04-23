
def add(newWord: str, mean: str, myDict: dict):
    myDict[newWord] = mean

def delete(newWord, myDict):
    if newWord not in myDict.keys():
        print(f"don't exist {newWord} in dictionary")
        return False 
    myDict.pop(newWord)

def edit(newWord, mean, myDict):
    myDict[newWord] = mean

def listed(myDict):
    for i in myDict:
        print(i)

def find(word, myDict):
    if word not in myDict.keys():
        print(f"don't exist {word} in dictionary")
        return False 
    print(f'{word}: {myDict[word]}')

    