class Person:
    def __init__(self, gender, age):
        self.gender = gender
        self.age = age

    def showData(self):
        print(f"Inside Person class gender is {self.gender} and age is {self.age}")


class Employee(Person):
    def __init__(self, gender, age, name, profession):
        super().__init__(gender, age)
        self.name = name
        self.profession = profession

    def showDetails(self):
        print("gender : ", self.gender)
        print("age : ", self.age)
        print("name : ", self.name)
        print("profession : ", self.profession)


obj1 = Employee("Male", 29, "Aman kaushik", "Software Engineer")
#print("Obj1 : ", obj1.showDetails())

print("Obj1.age : ", obj1.age)
print("obj1.gender : ", obj1.gender)
print("obj1.profession : ", obj1.profession)
print("obj1.name : ", obj1.name)
