class student:
     def __init__(self,rollno,name,age):
        self.rollno=rollno
        self.name=name
        self.age=age
        
     def display(self):
        print(f"roll no: {self.rollno}\nname:{self.name}\nage:{self.age}")
        
def get_name(student):
   return student.name
   
students=[]
n=int(input("enter the number of students:"))

for i in range(n):
   rollno=int(input(f"enter roll no for student  {i+1}:"))
   name=input(f"enter name for student {i+1}:")
   age=int(input(f"enter age for student {i+1}:"))
   students.append(student(rollno,name,age))
   
students.sort(key=get_name)
print("\nstudent details in ascending order of name:")
for student in students:
   student.display()
      
     
