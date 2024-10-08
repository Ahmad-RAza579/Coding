class Student:
    print('i am inside the class')
    def __init__(self,name):
        self.name=name
    
    def display(self):
        print("my name is",self.name)

a=Student("ahmed")
a.display()