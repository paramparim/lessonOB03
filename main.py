import pickle


# 1. Базовый класс Animal (Животное)
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        raise NotImplementedError("Этот метод должен быть переопределен в подклассах")

    def eat(self):
        print(f"{self.name} ест.")


# 2. Подклассы Bird (Птица), Mammal (Млекопитающее), Reptile (Рептилия)
class Bird(Animal):
    def __init__(self, name, age, wing_span):
        super().__init__(name, age)
        self.wing_span = wing_span

    def make_sound(self):
        print(f"{self.name} чирикает.")


class Mammal(Animal):
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color

    def make_sound(self):
        print(f"{self.name} рычит.")


class Reptile(Animal):
    def __init__(self, name, age, scale_type):
        super().__init__(name, age)
        self.scale_type = scale_type

    def make_sound(self):
        print(f"{self.name} шипит.")


# 3. Функция для демонстрации полиморфизма
def animal_sound(animals):
    for animal in animals:
        animal.make_sound()


# 4. Композиция: класс Zoo (Зоопарк)
class Zoo:
    def __init__(self):
        self.animals = []
        self.employees = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_employee(self, employee):
        self.employees.append(employee)

    def save_zoo(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self, file)

    @staticmethod
    def load_zoo(filename):
        with open(filename, 'rb') as file:
            return pickle.load(file)


# 5. Классы сотрудников
class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position


class ZooKeeper(Employee):
    def __init__(self, name):
        super().__init__(name, "Смотритель зоопарка")

    def feed_animal(self, animal):
        print(f"{self.name} кормит {animal.name}.")


class Veterinarian(Employee):
    def __init__(self, name):
        super().__init__(name, "Ветеринар")

    def heal_animal(self, animal):
        print(f"{self.name} лечит {animal.name}.")



# Создаем животных
bird = Bird("Попугай", 2, "20 см")
mammal = Mammal("Тигр", 4, "Оранжевый")
reptile = Reptile("Змея", 3, "Чешуйчатый")

# Демонстрируем полиморфизм
animals = [bird, mammal, reptile]
animal_sound(animals)

# Создаем сотрудников
zookeeper= ZooKeeper("Джон")
veterinarian = Veterinarian("Доктор Смит")

# Создаем зоопарк и добавляем животных и сотрудников
zoo = Zoo()
zoo.add_animal(bird)
zoo.add_animal(mammal)
zoo.add_animal(reptile)
zoo.add_employee(zookeeper)
zoo.add_employee(veterinarian)

# Сохраняем состояние зоопарка
zoo.save_zoo("zoo_state.pkl")

# Загружаем состояние зоопарка
loaded_zoo = Zoo.load_zoo("zoo_state.pkl")

for animal in loaded_zoo.animals:
    print(f"Загруженное животное: {animal.name}, Возраст: {animal.age}")

for employee in loaded_zoo.employees:
    print(f"Загруженный сотрудник: {employee.name}, Должность: {employee.position}")
