
class Employee:
    def setId(self, id):
        self.id = id
    def getId(self):
        return self.id

    def setName(self, name):
        self.name = name
    def getName(self):
        return self.name

    def setSalary(self, salary):
        self.salary = salary
    def getSalary(self):
        return self.salary

    def __init__(self, id: str, name: str, salary: int):
        self.id = id 
        self.name = name
        self.salary = salary

        self.employee = {
            "id": self.id,
            "Name": self.name,
            "Salary": self.salary
        }

    def raiseSalary(self, amount: float):
        self.salary += amount
    
    def showInfo(self):
        print(self.employee)
    
    def __lt__(self, other):
        return self.salary > other.salary


employee_1 = Employee("XXX", "Linh Vo", 1000)
employee_2 = Employee("XXX2", "Van A", 2000)
employee_3 = Employee("XXX3", "Van B", 3000)

listEmployee = [employee_1, employee_2, employee_3]

print("===== List Employee before short basr on salary =====")
for em in listEmployee:
    em.showInfo()

print("===== List Employee after short basr on salary =====")
listEmployee.sort()
for em in listEmployee:
    em.showInfo()
