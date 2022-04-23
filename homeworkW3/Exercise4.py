n = int(input('Enter n: \n'))

sum = 0
for i in range(1, n+1):
    sum += i

sum2 = 0
print("=============================")
for i in range(1, 2 * n + 2, 2):
    print(i)
    sum += 1/i

sum3 = 0
for i in range(1, n + 1):
    if (i % 2 != 0):
        sum3 += 1


def check_prime_number(n):
    flag = 1
    if (n <2):
        return False  
    
    for p in range(2, n):
        if n % p == 0:
            flag = False
            return flag
    return True

for i in range(n):
    if check_prime_number(i):
        print(i)


def find_square_number(n):
    flag = False

    if any(i**2 == n for i in range(n+1)):
        flag = True
    return flag

for i in range(n):
    if find_square_number(i):
        print(i)
