class Student:
    def __init__(self, name, rollno, marks):
        self.name = name
        self.rollno = rollno
        self.marks = marks
    
    def display(self):
        print(f"Name: {self.name}, Roll No: {self.rollno}, Marks: {self.marks}")

class Fees(Student):
    def __init__(self, name, rollno, marks):
        super().__init__(name, rollno, marks)
        self.fees = 0
    
    def submit_fees(self, amount):
        self.fees += amount
        return True
    
    def generate_receipt(self):
        print(f"Receipt - Roll No: {self.rollno}, Name: {self.name}, Fees Paid: {self.fees}")
    
class Result(Student):
    def __init__(self, name, rollno, marks):
        super().__init__(name, rollno, marks)
        self.grade = self.calculate_grade()
    
    def calculate_grade(self):
        if self.marks >= 90:
            return 'A'
        elif self.marks >= 80:
            return 'B'
        elif self.marks >= 70:
            return 'C'
        elif self.marks >= 60:
            return 'D'
        else:
            return 'F'
    
    # Method overriding
    def display(self):
        super().display()
        print(f"Grade: {self.grade}")

# Create students
students = []
n = int(input("Enter number of students: "))
for i in range(n):
    name = input(f"Enter name for student {i+1}: ")
    rollno = input(f"Enter roll number for student {i+1}: ")
    marks = float(input(f"Enter marks for student {i+1}: "))
    students.append(Result(name, rollno, marks))

# Sort by marks
print("\nStudents sorted by marks:")
for student in sorted(students, key=lambda s: s.marks, reverse=True):
    student.display()
    print()

# Sort by name
print("\nStudents sorted by name:")
for student in sorted(students, key=lambda s: s.name):
    student.display()
    print()
