# Exercise1: Compute 5!
fac = 1

for i in range(1, 6):
    fac = fac*i

print(f"5! = {fac}")

# Exercise2: sum 1 to 20
sum_ = 0

for i in range(1, 21):
    sum_ += i

print(f"Sum of 1 to 20 =  {sum_}")

# Exercise3: create list within 5 number and sum of list
numbers = [1,2,3,4,5]

print(f'Sum of list =  {sum(numbers)}')
