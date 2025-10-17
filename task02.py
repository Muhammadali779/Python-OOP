class Students:
    def __init__(self, name, age, grade):
        self.ismi = name
        self.yoshi = age
        self.kursi = grade

student1 = Students("Ali", 19, "2-kurs")
student2 = Students("Vali", 22, "4-kurs")
student3 = Students("Guli", 18, "1-kurs")

students_list = [student1, student2, student3]

for student in students_list:
    print(f"Talaba ismi: {student.ismi}, Yoshi: {student.yoshi} da, {student.kursi} talabasi")
