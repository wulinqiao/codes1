class Car():


    def __init__(self, color=None, band="Toyota"):
        """
        __init__ 的 Docstring
        
        :param self: 说明
        :param color: 说明
        """
        self.color = color
        self.band = band
        print("Car object is created")

    def __str__(self):
        return f"Car color is {self.color} and band is {self.band}HHHHH"

    def __del__(self):
        print()
        print(f"Car object {self} is being deleted")

c1 = Car("red", "Toyota")
c2 = Car("blue", "Honda")
# print(c1)
# print(c2)
# print("End of the program")


