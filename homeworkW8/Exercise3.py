fo = open("input.txt", mode="w")
test = 1
try:
    n = int(input("Enter n: "))
    test += int(n) + 1
except ValueError:
    print("n must be number")
    n = input("Enter again n: ")

for i in range(n):
    try:
        ele = int(input("Enter ele: "))
        test /= ele
    except ValueError:
        print("ele must be number")
        ele = int(input("Enter again ele: "))

    str_ele = str(ele) + " "

    fo.write(str_ele)