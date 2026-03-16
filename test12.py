class Student:
    school="ABC High School"
    @classmethod
    def show1(cls):
        print("School Name:", cls.school)
    @staticmethod
    def show2():
        print("This is a static method.")
if __name__=="__main__":
    s1=Student()
    s1.show1()
    s1.show2()