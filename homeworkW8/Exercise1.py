
test = 0
try:
    numerator = int(input("Enter numerator: "))
    test += int(numerator) + 1
except ValueError:
    print("Numerator must be number")
    numerator = input("Enter again numerator: ")

try:
    denominator = int(input("Enter denominator: "))
    test /= denominator
except ZeroDivisionError:
    print("denominator is 0")
    denominator = input("Enter agian denominator: ")
except ValueError:
    print("Denominator must be number")
    denominator = int(input("Enter again denominator: "))

print(f"a/b = {numerator/denominator}")