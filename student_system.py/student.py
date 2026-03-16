class Student:
    def __init__(self, name, gender, age, phonenumber,describe):
        self.name = name
        self.gender = gender
        self.age = age
        self.phonenumber = phonenumber
        self.describe = describe

    def __str__(self):
        return f"Name: {self.name}, Gender: {self.gender}, Age: {self.age}, Phone Number: {self.phonenumber}, Describe: {self.describe}"
