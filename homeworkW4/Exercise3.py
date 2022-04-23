
format = ['/', '[', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+']

def checkPassword(password: str):
    lenString = len(password)
    checkLower = 0
    checkUpper = 0
    checkNumber = 0
    checkEspecial = 0

    if lenString > 12 and lenString < 6:
        print("length password must be larger than 6 and smaller than 12")
        return False

    for c in password:
        if c.islower():
            checkLower += 1
        if c.isupper():
            checkUpper += 1
        if c.isnumeric():
            checkNumber += 1
        if c in format:
            checkEspecial += 1

    if checkLower == 0 or checkUpper == 0 or checkNumber == 0 or checkEspecial == 0:
        print('Password does not satisfy the condition')
        return False
    
    return True


