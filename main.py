# 3. Продемонстрируйте полиморфизм: создайте функцию `animal_sound(animals)`,
# которая принимает список животных и вызывает метод `make_sound()` для каждого животного.
#
# 4. Используйте композицию для создания класса `Zoo`, который будет содержать информацию
# о животных и сотрудниках. Должны быть методы для добавления животных и сотрудников в зоопарк.
#
# 5. Создайте классы для сотрудников, например, `ZooKeeper`, `Veterinarian`,
# которые могут иметь специфические методы (например, `feed_animal()` для `ZooKeeper`
# и `heal_animal()` для `Veterinarian`).

class Animal:
    def __int__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass

    def eat(self):
        pass


class Bird(Animal):
    def make_sound(self):
        print("Чирик-чирик")
        print("1")
        #return "Чирик-чирик"

    def eat(self):
        print("Птичка клюет")
        print("2")


class Mammal(Animal):
    def make_sound(self):
        print("Му-му")
        print("3")
        return "Му-му"

    def eat(self):
        print("Животное ест")
        print("4")


class Reptile(Animal):
    def make_sound(self):
        print("ШШШШШ")
        print("5")
        return "ШШШШШ"

    def eat(self):
        print("Ням-ням")
        print("6")


animals = [Bird(), Mammal(), Reptile()]
for animal in animals:
    animal.make_sound()
    animal.eat()


bird1 = Bird()
mammal1 = Mammal()
reptile1 = Reptile()


# def animal_sound(animals):
#     print("def animal_sound")
#
#     for animal in animals:
#         print("in cycle")
#
#         print(animal.make_sound())

def animal_sound(animals):
    for animal in animals:
        print(f"{animal.name}: {animal.make_sound()}")

# Пример использования
#zoo = Zoo()
bird1 = Bird("Косяк", 2)
mammal1 = Mammal("Корова", 5)
reptile1 = Reptile("Уж", 3)


animal_sound(animals)