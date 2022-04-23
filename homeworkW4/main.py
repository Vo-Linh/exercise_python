
from Exercise2 import *
from Exercise3 import checkPassword
from Exercise1 import *
from Exercise4 import *


print('================= Exercise 1 ================')
myArray = []
 
# number of elements as input
n = int(input("Enter number of elements : "))
 
# iterating till the range
for i in range(0, n):
    ele = int(input())
    myArray.append(ele) # adding the element

print(f"Max number: {findMax(myArray)}")
print(f"Seccond number: {findSeccond(myArray)}")
print(f"sum prime number: {sumPrimeNumber(myArray= myArray)}")
X = int(input("Enter X: \n"))
print(f"Element larger than X {findNumberLargerX(myArray, X)}")
print(f"Sort array \n {sortList(myArray)}")
print(f"Frequency: \n {frequency(myArray= myArray)}")

print('================= Exercise 2 ================')
name = input('Enter name: \n')

newName = Normailize(name)
print(newName)        
print("Output character to line")
for c in newName:
    for i  in c:
        print(i)

print("Output word by line")
for i in newName:
    if (i != " "):
        print(i)

print("==============================")
for i in range(-len(newName) + 1, 1):
    print(newName[-i])


print('=================================')

ten_dem = ''
for i in range(1, len(newName)-1):
    ten_dem += newName[i] + ' '

print(f'Ho: {newName[0]}')
print(f'Ten: {newName[-1]}')
print(f'Ten Dem: {ten_dem}')

print('================= Exercise 3 ================')
password = input('Enter password: \n')

if checkPassword(password):
    print(f'Your password: {password}')

print("================= Exercise 4 ================")
myDict = {
    'hello': 'xin chao'
}

add("Hi", 'Xin chao', myDict)
delete("Hi", myDict= myDict)
