class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"
class Cat(Animal):
    def speak(self):
        return "Meow!"
class Car:
    def speak(self):
        return "Vroom!"

def animal_sound(ani:Animal) -> str:
    return ani.speak()
if __name__ == "__main__":
    dog = Dog()
    cat = Cat()
    car = Car()
    print(animal_sound(dog))  # Output: Woof!
    print(animal_sound(cat))  # Output: Meow!
    print(animal_sound(car))  # Output: Vroom!