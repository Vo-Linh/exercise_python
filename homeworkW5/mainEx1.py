from Exercise2 import *

Array = []
 
# number of elements as input
n = int(input("Enter number of elements : "))
 
# iterating till the range
for i in range(0, n):
    ele = int(input())
    Array.append(ele) # adding the element

num2st = findSeccond(myArray= Array)
print(Array)
print(num2st)