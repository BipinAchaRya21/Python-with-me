# OOPs (Object Orinted Programming ) -> it is a programming paradigm 
# based on the concept of objects, which can contain 
# data and code: data in the form of fields 
# (often known as attributes), and code, in the form of 
# procedures (often known as methods).

class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def introduce(self):
        print("My name is", self.name)
        print("I am", self.age, "years old")

student1 = Student("Bipin", 22)
student1.introduce()