
from exercise2 import*

n = int(input("Enter number student: "))

listStudent = []

for _ in range(n):
    id = input("Id: ")
    studentID = input("Student id: ")
    name = input("Name: ")
    age = int(input("Age: "))
    scoreTotal = float(input("Score total: "))
    print("==============================")
    student = Student(studentID, id, name, age, scoreTotal)
    listStudent.append(student)

listStudent.sort()
print("========= List Student ============")
for stu in listStudent:
    stu.printInfo()