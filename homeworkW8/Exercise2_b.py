
fo = open("input.txt", mode = 'r')
str_value = fo.read()
value = str_value.split()

print(value)
sum = 0
mul = 1
for i in value:
    sum += int(i)
    mul *= int(i)

if len(value) == 2:
    print(f"a + b = {sum}, a * b = {mul}")
else:
    print(f"sum of {len(value)} ele = {sum}, Multiply of {len(value)} ele = {mul}")