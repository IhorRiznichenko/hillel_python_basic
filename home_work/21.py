class Auto:
    def __init__(self, brand, age, color, mark, weight):
        self.brand = brand
        self.age = age
        self.color = color
        self.mark = mark
        self.weight = weight

    def move(self):
        print("move")

    def birthday(self):
        self.age += 1

    def stop(self):
        print("stop")

class Truck(Auto):
    def __init__(self, brand, age, color, mark, weight, max_load):
        super().__init__(brand, age, color, mark, weight)
        self.max_load = max_load

    def move(self):
        print('attention')
        super().move()

    def load(self):
        import time
        time.sleep(1)
        print('load')
        time.sleep(1)


class Car(Auto):
    def __init__(self, brand, age, color, mark, weight, max_speed):
        super().__init__(brand, age, color, mark, weight)
        self.max_speed = max_speed

    def move(self):
        super().move()
        print(f'max speed is {self.max_speed}')

t1 = Truck('Volvo', 2, 'red', 'truck', 1000, 5000)
t2 = Truck('Scania', 5, 'blue', 'truck', 2000, 10000)

c1 = Car('BMW', 1, 'black', 'sedan', 1200, 200)
c2 = Car('Audi', 3, 'white', 'hatchback', 1300, 180)

print(t1.brand)
print(c2.age)
print(t2.max_load)

t1.move()
t1.load()
t1.birthday()
print(t1.age)

c2.move()
c2.birthday()
c2.move()
