class Father:
    def __init__(self):
        self.gender ="Male"

    def walk(self):
        print("hahaha")
class Son(Father):
    pass
s = Son()
print(f"gender: {s.gender}")
s.walk()