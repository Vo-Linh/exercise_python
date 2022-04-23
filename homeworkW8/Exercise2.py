fo = open("input.txt", mode="w")

test = 1
try:
    a = int(input("Enter a: "))
    test += int(a) + 1
except ValueError:
    print("a must be number")
    a = input("Enter again a: ")

try:
    b = int(input("Enter b: "))
    test /= b
except ZeroDivisionError:
    print("b is 0")
    b = input("Enter agian b: ")
except ValueError:
    print("b must be number")
    b = int(input("Enter again b: "))

str_a = str(a) + " "
str_b = str(b) + "\n"

fo.write(str_a)
fo.write(str_b)


