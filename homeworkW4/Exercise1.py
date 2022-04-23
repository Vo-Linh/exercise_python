
def mySplit(name, delimiters=' \t\n'):
    result = []
    word = ''
    for c in name:
        if c not in delimiters:
            word += c
        elif word:
            result.append(word)
            word = ''

    if word:
        result.append(word)

    return result

def listToString(s): 
    # initialize an empty string
    str1 = "" 
    # traverse in the string  
    for ele in s: 
        str1 += ele  
    
    return str1

def Normailize(name):
    splitName = mySplit(name)

    newName = []
    for c in splitName:
        newC = []
        for i in range(len(c)):
            if i == 0:
                newC.append(c[0].upper())
            else:
                newC.append(c[i].lower())
        nameString = listToString(newC)

        newName.append(nameString)

    return newName

    
