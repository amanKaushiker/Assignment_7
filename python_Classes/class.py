class Person:
    def __init__(name,age,profession):
        self.name = name
        self.age = age
        self.profession = profession
        
    def greet(self):
        return   f"Hello, my name is {self.name} and I am {self.age} years old."
    
person1 = Person("Alice", 30)
      
print(person1.greet())      