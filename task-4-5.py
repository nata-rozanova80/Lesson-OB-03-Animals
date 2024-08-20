# 4. Используйте композицию для создания класса `Zoo`, который будет содержать информацию
# о животных и сотрудниках. Должны быть методы для добавления животных и сотрудников в зоопарк.
#
# 5. Создайте классы для сотрудников, например, `ZooKeeper`, `Veterinarian`,
# которые могут иметь специфические методы (например, `feed_animal()` для `ZooKeeper`
# и `heal_animal()` для `Veterinarian`).

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


# Зоопарк
class Zoo:
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_staff(self, staff_member):
        self.staff.append(staff_member)

# Сотрудники
class ZooKeeper:
    def feed_animal(self, animal):
        print(f"Смотритель кормит: {animal.eat()}")

class Veterinarian:
    def heal_animal(self, animal):
        print(f"Ветеринар лечит: {animal.name}")



zoo = Zoo()
bird1 = Bird("Косяк", 2)
mammal1 = Mammal("Корова", 5)
reptile1 = Reptile("Уж", 3)

zoo.add_animal(bird1)
zoo.add_animal(mammal1)
zoo.add_animal(reptile1)

zookeeper = ZooKeeper()
veterinarian = Veterinarian()

# Кормление и лечение
zookeeper.feed_animal(bird1)
veterinarian.heal_animal(mammal1)



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
