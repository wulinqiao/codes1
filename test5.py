class Father(object):
    def __init__(self):
        self.gender ="Male"
class Mother(object):
    def __init__(self):
        self.gender ="Female"
class Child(Mother,Father):
    pass
c = Child()
print(f"gender: {c.gender}")