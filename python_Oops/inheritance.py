class Employee:
    def __init__(self, name , age):
        self.name = name
        self.age = age
        
    def showDetails(self):
        print(f"Name is {self.name} & age is {self.age}")
        
class Programmer:
    def showLang(self):
        print(self.name)        
        
e1 = Employee("Aman kaushik", 29)
e1.showDetails()        

e2 = Programmer()
e2.showLang()