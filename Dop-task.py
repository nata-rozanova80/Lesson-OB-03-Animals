# Попробуйте добавить дополнительные функции в вашу программу, такие как сохранение информации о зоопарке в файл
# и возможность её загрузки, чтобы у вашего зоопарка было "постоянное состояние" между запусками программы.

import json

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass

    def eat(self):
        pass

    # 'type': self.__class__.__name__: Эта строка создает пару "ключ-значение", где ключ — строка 'type', а
    # значение — имя класса текущего экземпляра.self.__class__ возвращает класс экземпляра, а  __name__ — его
    # имя в виде строки.Таким образом, эта строка позволяет сохранить тип  животного(например, Bird, Mammal, Reptile)
    # в словаре.
    def to_dict(self):
        return {
            'name': self.name,
            'age': self.age,
            'type': self.__class__.__name__
        }
    # В результатe метод to_dict создает словарь, который содержит информацию о животном: его имя, возраст и тип.
    # Этот  словарь можно использовать для  сериализации(например, для сохранения в файл в формате JSON), что
    # позволяет легко  сохранять  и восстанавливать  состояние  объектов.

    # Комментарии к этому методу смотри в readme файле
    @classmethod
    def from_dict(cls, data):
        return cls(data['name'], data['age'])


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
        print(f"Рептилия ням-ням")


class Zoo:
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_staff(self, staff_member):
        self.staff.append(staff_member)

    def save_to_file(self, filename):
        with open(filename, 'w') as f:
            json.dump([animal.to_dict() for animal in self.animals], f)

    def load_from_file(self, filename):
        with open(filename, 'r') as f:
            animal_data = json.load(f)
            for data in animal_data:
                if data['type'] == 'Bird':
                    self.add_animal(Bird.from_dict(data))
                elif data['type'] == 'Mammal':
                    self.add_animal(Mammal.from_dict(data))
                elif data['type'] == 'Reptile':
                    self.add_animal(Reptile.from_dict(data))


class ZooKeeper:
    def feed_animal(self, animal):
        print(f"Смотритель кормит: {animal.eat()}")

class Veterinarian:
    def heal_animal(self, animal):
        print(f"Ветеринар лечит: {animal.name}")


# Пример использования
zoo = Zoo()
bird1 = Bird("Воробей", 2)
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

# Сохранение состояния зоопарка в файл
zoo.save_to_file('zoo_data.json')

# Загрузка состояния зоопарка из файла
new_zoo = Zoo()
new_zoo.load_from_file('zoo_data.json')

# Проверка загруженных данных
for animal in new_zoo.animals:
    animal.make_sound()
    animal.eat()
