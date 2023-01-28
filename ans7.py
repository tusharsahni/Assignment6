class Student:
    pass

class Marks:
    pass

Tushar=Student()

Tushar_ke_marks=Marks()

print("Tushar is an instance of class Student:",isinstance(Tushar,Student))
print("Tushar is an instance of class Marks:",isinstance(Tushar,Marks))
print("Tushar_ke_marks is an instance of class Student:",isinstance(Tushar_ke_marks,Student))
print("Tushar_ke_marks is an instance of class Marks:",isinstance(Tushar_ke_marks,Marks))

print("Student is a subclass of class object:",issubclass(Student,object))
print("Marks is a subclass of class object:",issubclass(Marks,object))
