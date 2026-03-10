class Student:
    def __init__(self, student_id, name, age):
        self.student_id = student_id
        self.name = name
        self.age = age

    def display(self):
        print(f"Student ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


class Mark(Student):
    def __init__(self, student_id, name, age, marks):
        super().__init__(student_id, name, age)  # Call superclass constructor
        self.marks = marks  # Store marks

    def calculate(self):
        avg = sum(self.marks) / len(self.marks)  
        
        
        if avg >= 90:
            grade = "A+"
        elif avg >= 80:
            grade = "A"
        elif avg >= 70:
            grade = "B"
        elif avg >= 60:
            grade = "C"
        elif avg >= 50:
            grade = "D"
        else:
            grade = "Fail"
        
        self.display()  # Display student details
        print(f"Marks: {self.marks}")
        print(f"Average: {avg:.2f}")
        print(f"Grade: {grade}")


student_id = input("Enter Student ID: ")
name = input("Enter Name: ")
age = int(input("Enter Age: "))
marks = list(map(int, input("Enter marks separated by spaces: ").split()))


student = Mark(student_id, name, age, marks)
student.calculate() 