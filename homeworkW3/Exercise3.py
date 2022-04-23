# Exercise 1: Compute S =  1 + (2*1)/(2*1 - 1) + (2+4)/(1+3) + (2+4+6)/(1+3+5) + … (2+4+...+2n)/(1+3+...+(2n-1))
print("============= Exercise 1 ==========================")
n = int(input("Enter n \n"))

total = 1
sumTop = 2
sumBottom = 1
indexTop = 2
indexBottom = 1

for _ in range(n):

    indexTop += 2
    indexBottom += 2
    sumTop += indexTop
    sumBottom += indexBottom

    if (indexTop <= 2*n and indexBottom <= 2*n-1):
        total += float(sumTop)/sumBottom

print(f"Total = {total}")
