
class People:
    def __init__(self, id: str, name: str, age: int):
        self.id = id
        self.name = name 
        self.age = age

class Student(People):
    def __init__(self,studentID:str, id: str, name: str, age: int, scoreTotal: float):
        super().__init__(id, name, age)
        self.studenID = studentID
        self.scoreTotal = scoreTotal

    def printInfo(self):
        print(f"""
            Id: {self.id} \n
            Itudent id: {self.studenID} \n
            Name: {self.name} \n
            Age: {self.age} \n
            Score Avg: {self.scoreTotal} \n
            ============================== \n
        """)
    
    def Total(self) -> float:
        return self.scoreTotal

    def __lt__(self, other):
        return self.scoreTotal > other.scoreTotal


