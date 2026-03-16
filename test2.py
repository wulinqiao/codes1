class Student:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
    def __str__(self):
        return f"Student {self.name} weight is {self.weight}"
    def run(self):
        self.weight -= 1
        print(f"Student {self.name} is running, weight is now {self.weight}")
    def eat(self):
        self.weight += 2
        print(f"Student {self} is eating, weight is now {self.weight}")

s1 = Student("a",150)
print(s1)
s1.run()
s1.eat()
print('after running and eating')
