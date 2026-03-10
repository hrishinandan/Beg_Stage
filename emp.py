# define a python class employee with attributes(emp id,emp_name,basic_salary)
# find the net salary of the employee
# net salary = DA+HRA+BAsic_salary
class Emp:
    def __init__(self):  
        self.emp_id = int(input("Enter the employee ID: "))
        self.emp_name = input("Enter the name: ")
        self.basic_salary = int(input("Enter the basic salary: "))

    def totalsal(self):  
        self.HRA = 0.4*self.basic_salary
        print("HRA",self.HRA)
        self.DA = 0.5*self.basic_salary
        print("Da",self.DA)
        self.net_salary = self.HRA + self.DA + self.basic_salary
        print("Net Salary:", self.net_salary)

employee = Emp()  
employee.totalsal()  



