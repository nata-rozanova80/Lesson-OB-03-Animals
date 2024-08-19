class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass

    def eat(self):
        pass


class Bird(Animal):
    def make_sound(self):
        sound = "Чирик-чирик"
        print(f"{self.name} (птица) говорит {sound}")

    def eat(self):
        print("Птица клюет")


class Mammal(Animal):
    def make_sound(self):
        sound = "Му-му"
        print(f"{self.name} (млекопитающее) говорит {sound}")

    def eat(self):
        print("Животное ест")



class Reptile(Animal):
    def make_sound(self):
        sound = "ШШШШ"
        print(f"{self.name} (рептилия) говорит {sound}")

    def eat(self):
        print(f"Pептилия ням-ням")


def animal_sound(animals):
    for animal in animals:
        animal.make_sound()

# Создаем экземпляры животных
animals = [Bird("Синица", 1), Mammal("Корова", 2), Reptile("Ящерица", 3)]

# Вызываем функцию animal_sound
animal_sound(animals)

# Показываем, как они едят
for animal in animals:
    animal.eat()
