class Student:
    pass

class Marks:
    pass

sambhav=Student()

sambhav_ke_marks=Marks()

print("Tushar is an instance of class Student:",isinstance(tushar,Student))
print("Tushar is an instance of class Marks:",isinstance(tushar,Marks))
print("tushar_ke_marks is an instance of class Student:",isinstance(tushar_ke_marks,Student))
print("tushar_ke_marks is an instance of class Marks:",isinstance(tushar_ke_marks,Marks))

print("Student is a subclass of class object:",issubclass(Student,object))
print("Marks is a subclass of class object:",issubclass(Marks,object))