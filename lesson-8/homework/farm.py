class Animal:
    def __init__(self, name, age, sound):
        self.name = name
        self.age = age
        self.sound = sound

    def make_sound(self):
        return f"{self.name} says {self.sound}!"

    def eat(self, food):
        return f"{self.name} is eating {food}."

    def sleep(self):
        return f"{self.name} is sleeping."

class Cow(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, "Moo")

    def produce_milk(self):
        return f"{self.name} is producing milk."

class Chicken(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, "Cluck")

    def lay_egg(self):
        return f"{self.name} has laid an egg."

class Sheep(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, "Baa")

    def shear(self):
        return f"{self.name} is being sheared for wool."

# Example Usage:
cow = Cow("Bessie", 5)
chicken = Chicken("Henrietta", 2)
sheep = Sheep("Dolly", 3)

print(cow.make_sound())
print(chicken.eat("corn"))
print(sheep.sleep())
print(cow.produce_milk())
print(chicken.lay_egg())
print(sheep.shear())
