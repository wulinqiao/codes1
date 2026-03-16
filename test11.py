class Student:
    
    teacher = "Mr. Smith"
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    def __str__(self):
        return f"name: {self.name}, teacher: {self.teacher}, age: {self.age}, grade: {self.grade}"
if __name__ == "__main__":
        
        student1 = Student("Alice", 20, "A")
        student2 = Student("Bob", 22, "B")
        Student.teacher = "Ms. Johnson"
        print(student1)
        print(student2)
        student1.teacher = "Ms. Johnson"
