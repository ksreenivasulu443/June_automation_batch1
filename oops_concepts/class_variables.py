class Student:
    college_name = 'SSBN' # class variable
    def __init__(self,name, marks): # constructor method
        self.name=name # instance variable
        self.marks =marks # instance variable
        Student.department_hod ='XYZ' # class variable
        print("class variable access from constructor using class name", Student.college_name)
        print("class variable access from constructor using self", self.college_name)

    def student_info_display(self): # instance method
        self.department='ECE' # instance variable
        Student.professor = 'KLM' #class variable
        print(f"Student name {self.name} and marks are {self.marks}") # we are accessing instance variable using self keyword
        print("class variable access from instance method using class name", Student.college_name)
        print("class variable access from instance method using self", self.department_hod)

    @classmethod
    def college_info_display(cls): #class method
        Student.total_student = 438 # class variable
        cls.number_employee = 45 # class variable
        print("college nam is", cls.college_name)
        print("class variable access from class method using class name", Student.college_name)
        print("class variable access from class method using cls", cls.college_name)

    @staticmethod
    def private_college_info(): #static method
        Student.private_variable = 'private' # class variable
        private_college_number = 9642289832 # local variable
        print("this is private college info method")
        print("class variable access from static method using class name", Student.college_name)




student_object = Student('sreeni', 67)

# print("student name using object reference", student_object.name)
student_object.student_info_display()
student_object.college_info_display()
student_object.private_college_info()
print("class variable access outside of the class using class name", Student.college_name)
print("class variable access outside of the class using object reference", student_object.college_name)

