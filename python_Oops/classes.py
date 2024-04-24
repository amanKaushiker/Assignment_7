class Person:
    name = "Aman"
    occupation = "Software Engineer"
    networth = 20

    def info(self):
        print(f"{self.name} is a {self.occupation} has netwoth of {self.networth}")


a = Person()
a.info()

a.name = "Ayush"
a.occupation = "Software Developer"
a.networth = 100

a.info()
