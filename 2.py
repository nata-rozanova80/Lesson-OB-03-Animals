import json


class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass

    def eat(self):
        pass

    def to_dict(self):
        return {
            'name': self.name,
            'age': self.age,
            'type': self.__class__.__name__
        }

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

    def display_data(self):
        print("Животные в зоопарке:")
        for animal in self.animals:
            print(f"Тип: {animal.__class__.__name__}, Имя: {animal.name}, Возраст: {animal.age}")

        print("\nСотрудники в зоопарке:")
        for staff_member in self.staff:

            print(f"Тип: {staff_member.__class__.__name__}")


class ZooKeeper:
    def feed_animal(self, animal):
        print(f"Смотритель кормит: {animal.eat()}")


class Veterinarian:
    def heal_animal(self, animal):
        print(f"Ветеринар лечит: {animal.name}")


# Функции для ввода новых животных и сотрудников
def input_animal():
    animal_type = input("Введите тип животного (Bird, Mammal, Reptile): ")
    name = input("Введите имя животного: ")
    age = int(input("Введите возраст животного: "))

    if animal_type.lower() == 'bird':
        return Bird(name, age)
    elif animal_type.lower() == 'mammal':
        return Mammal(name, age)
    elif animal_type.lower() == 'reptile':
        return Reptile(name, age)
    else:
        print("Неверный тип животного.")
        return None


def input_staff():
    staff_type = input("Введите тип сотрудника (ZooKeeper, Veterinarian): ")
    name = input("Введите имя сотрудника: ")

    if staff_type.lower() == 'zookeeper':
        return ZooKeeper()  # Можно добавить атрибуты, если необходимо
    elif staff_type.lower() == 'veterinarian':
        return Veterinarian()  # Можно добавить атрибуты, если необходимо
    else:
        print("Неверный тип сотрудника.")
        return None


# Пример использования
zoo = Zoo()

# Ввод животных
num_animals = int(input("Сколько животных вы хотите добавить? "))
for _ in range(num_animals):
    animal = input_animal()
    if animal:
        zoo.add_animal(animal)

# Ввод сотрудников
num_staff = int(input("Сколько сотрудников выхотите добавить? "))
for _ in range(num_staff):
    staff_member = input_staff()
    if staff_member:
        zoo.add_staff(staff_member)

# Вывод всех данных по запросу
if zoo.animals or zoo.staff:
    zoo.display_data()

# Кормление и лечение
if zoo.animals:
    zookeeper = ZooKeeper()
    veterinarian = Veterinarian()
    zookeeper.feed_animal(zoo.animals[0])  # Кормим первого животного
    veterinarian.heal_animal(zoo.animals[0])  # Лечим первого животного

# Сохранение состояния зоопарка в файл
zoo.save_to_file('zoo_data.json')

# Загрузка состояния зоопарка из файла
new_zoo = Zoo()
new_zoo.load_from_file('zoo_data.json')

# Проверка загруженных данных
for animal in new_zoo.animals:
    animal.make_sound()
    animal.eat()