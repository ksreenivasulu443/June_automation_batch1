"""This module is created to practice OOPS Concepts in python
created by Chandan on 24-07-2024"""

#above is called as "Documentation String"

class Student:
    college_name = 'SSBN' #class variable #created outside of methods & inside class
    def __init__(self,name,marks): #constructor
        self.name = name #instance variable
        self.marks = marks #instance variable
        Student.department_hod = 'xyz' #class variable #can be created inside constructor
        print("inside constructor - class variable using class name:",Student.college_name) #accessing class variable inside constructor
        print("inside constructor - class variable using self:", self.college_name)

    def student_info_display(self): #instance method #atleast one instance variable
        self.department = 'ECE' #instance variable
        Student.proffesor = 'klm' #class variable #can be created inside method
        #print(f"student name {self.name} and marks are {self.marks}") #here we are accessing instance variable
        #print(self.college_name)
        print("inside instance method - class variable using class name:",Student.college_name)
        print("inside instance method - class variable using self:", self.college_name)
        print("department_hod name:",Student.department_hod, self.department_hod)
        #class variable created can be accessed inside method using class or self keyword

    @classmethod
    def college_info_display(cls):
        Student.total_student = 438 #class variable #created using class name
        cls.number_of_employees = 45 #class variable #created using cls variable
        print("College name is:", cls.college_name)
        print("inside instance method - class variable using class name:", Student.college_name)
        print("inside instance method - class variable using self:", cls.college_name)

    @staticmethod
    def private_college_info():
        Student.private_variable = 'private' #class variable #created under static method
        print("this is private college info method")
        print("inside instance method - class variable using class name:", Student.college_name)
        #here inside static method, we can access class variable only using class_name

student_object = Student('Darshan','98')
#print("student name is:",student_object.name) #accessing instance variable using object reference
student_object.student_info_display()
student_object.private_college_info()
print("print class variable using class_name:",Student.college_name)
print("print class variable using object reference:",student_object.college_name)
print("print class variable using class_name:",Student.department_hod)
print("print class variable using object reference:",student_object.department)
print("print class variable using class_name:",Student.proffesor)
print("print class variable using object reference:",student_object.proffesor)

