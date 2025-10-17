class Student:

    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def info(self):
        print(f"{self.name}, {self.age} yoshda, {self.grade} o`quvchisi.")

student1 = Student("Ali", 15, "9-sinf")
student2 = Student("Vali", 16, "10-sinf")
student3 = Student("G`ani", 14, "8-sinf")

Students = [student1, student2, student3]

for s in Students:
    s.info()