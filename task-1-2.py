# 1. Создайте базовый класс `Animal`, который будет содержать общие атрибуты
# (например, `name`, `age`) и методы (`make_sound()`, `eat()`) для всех животных.
#
# 2. Реализуйте наследование, создав подклассы `Bird`, `Mammal`, и `Reptile`,
# которые наследуют от класса `Animal`. Добавьте специфические атрибуты и
# переопределите методы, если требуется (например, различный звук для `make_sound()`).

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

    def eat(self):
        print("Птичка клюет")


class Mammal(Animal):
    def make_sound(self):
        print("Му-му")

    def eat(self):
        print("Животное ест")


class Reptile(Animal):
    def make_sound(self):
        print("ШШШШШ")

    def eat(self):
        print("Ням-ням")


animals = [Bird(), Mammal(), Reptile()]
for animal in animals:
    animal.make_sound()
    animal.eat()