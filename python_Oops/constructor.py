class Person:
    def __init__(self, arg1, arg2):
        print("Hey this is constructor")
        self.name = arg1
        self.age = arg2
        
    def info(self):
        print(f"{self.name} is {self.age} years old") 
        
        
a = Person("Aman kaushik", 30 )
b = Person("ayush goel" , 29) 

a.info()
b.info()          