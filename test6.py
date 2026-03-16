class Father:
    def __init__(self):
        self.gender = "male"

class Mother:
    def __init__(self):
        self.gender = "female" 

class Child(Father, Mother):
    def __init__(self):
        Mother.__init__(self)   
        
a=Child()

print(a.gender)