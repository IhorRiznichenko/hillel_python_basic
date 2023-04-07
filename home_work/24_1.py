class Car:
    fuel_types = ['бензин', 'дизель', 'электричество', 'гибрид']
    colors = ['черный', 'белый', 'серебристый', 'синий', 'красный']

    def __init__(self, make, model, year, fuel_type, color):
        self.make = make
        self.model = model
        self.year = year
        if fuel_type in Car.fuel_types:
            self.fuel_type = fuel_type
        else:
            self.fuel_type = 'бензин'
        if color not in Car.colors:
            Car.colors.append(color)
        self.color = color

    def __str__(self):
        return f"{self.make} {self.model} {self.year}"

    @staticmethod
    def is_valid_fuel_type(fuel_type):
        return fuel_type in Car.fuel_types

    @classmethod
    def get_fuel_type_count(cls):
        return len(cls.fuel_types)

    @classmethod
    def get_color_count(cls):
        return len(cls.colors)

car1 = Car("Toyota", "Camry", 2020, "бензин", "синий")
car2 = Car("Tesla", "Model S", 2021, "электричество", "белый")
car3 = Car("Ford", "Mustang", 2022, "газ", "красный")
car4 = Car("Honda", "Civic", 2023, "бензин", "зеленый")
car5 = Car("BMW", "X5", 2022, "дизель", "красный")

print(Car.get_fuel_type_count())
print(Car.get_color_count())

print(car1.is_valid_fuel_type("бензин"))
print(car2.is_valid_fuel_type("дизель"))
