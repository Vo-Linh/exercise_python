# Exercise 2
print("============= Exercise 2 ==========================")

array = [1, 3, 5, 2, 4, 5]
array_ = array
array_.sort()

max = array_[-1]
count = 0

print(f'largest element in array: {max}')

for i in array_:
    if max == i:
        count += 1

print(f"2nd largest element in array: {array_[-count - 1]}")
print(f"Array after sorted: {array_}")

def primeNumber(a):
    '''
    check a is prime number 
    return True if a is prime number 
    return False if a isn't
    '''
    count = 0
    for i in range(1, a + 1):
        if a % i == 0:
            count += 1

    if count == 2:
        return True
    elif a == 1:
        return False
    else:
        return False

arrayPrimeNumber = []
for i in array:
    if primeNumber(i):
        arrayPrimeNumber.append(i)

print(f"Sum of prime number in array = {sum(arrayPrimeNumber)}")

x = int(input("Enter X: \n"))

arrayCompare = []
for i in array:
    if i > x:
        arrayCompare.append(i)

print(f"Element of array > X: {arrayCompare}")