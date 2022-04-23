

def findMax(myArray):
    MAX = myArray[0]
    lenmyArray = len(myArray)

    # Find max number
    for i in range(lenmyArray):
        if (myArray[i] > MAX):
            MAX = myArray[i]

    return MAX
    
def sortList(myArray):
    for i in range(len(myArray)):
       #Luu vi tri nho nhat
       viTriNhoNhat = i
       for j in range(i + 1, len(myArray)):
           if myArray[j] < myArray[viTriNhoNhat]:
               viTriNhoNhat = j
       #Doi vi tri phan tu thu i dang xet voi phan tu nho nhat
       myArray[i], myArray[viTriNhoNhat] = myArray[viTriNhoNhat], myArray[i]

    return myArray 

def findSeccond(myArray):
    MAX = findMax(myArray)
    # Sort myArray
    myArray.sort(reverse= False)

    # Find seccond number
    count = 0
    lenmyArray = len(myArray)
    for i in range(lenmyArray):
        if myArray[i] == MAX:
            count += 1
    
    return myArray[- count - 1]


def check_prime_number(n):
    flag = 1
    if (n <2):
        return False  
    
    for p in range(2, n):
        if n % p == 0:
            flag = False
            break 
    return True

def sumPrimeNumber(myArray):
    sum = 0
    for i in myArray:
        if check_prime_number(i):
            sum =+ i

    return sum
    

# Find number larger than X
def findNumberLargerX(myArray, X):
    print("Element larger than X")
    for i in myArray:
        if i > X:
            print(i)

#  frequency
def frequency(myArray):     
    frequency = {}
    for i in myArray:
        if i not in frequency.keys():
            frequency[i] = 1
        else:
            frequency[i] += 1
    return frequency

