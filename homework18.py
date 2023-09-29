import csv


class Car:
    car_instances = []

    def __init__(self, producer, brand, year_of_release=2020, fuel_consumption: float = 0.0):
        self.producer = producer
        self.brand = brand
        self.year_of_release = year_of_release
        self.fuel_consumption = fuel_consumption
        self.run = 0
        with open("car_info.csv", newline='', mode="a") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow([self.brand, self.producer, "scrapped"])
        Car.car_instances.append(self)

    def __str__(self):
        return f'Car {self.brand}'

    __repr__ = __str__

class Lorry(Car):
    def __init__(self, producer, brand, year_of_release=2020, fuel_consumption: float = 0.0,
                 cargo_capacity: float = 0.0):
        super().__init__(producer, brand, year_of_release, fuel_consumption)
        self.cargo_capacity = cargo_capacity


class SportsCar(Car):
    def __init__(self, producer, brand, year_of_release=2020, fuel_consumption: float = 0.0, max_speed: float = 0.0,
                 price: float = 0.0):
        super().__init__(producer, brand, year_of_release, fuel_consumption)
        self.max_speed = max_speed
        self.price = price


car = Car("Toyota", "Camry", 2022, 7.5)
car2 = Car("Honda", "Civic", 2021, 6.8)
car3 = Car("Volkswagen", "Phaeton", 2023, 9.1)
car4 = Car("Volkswagen", "Passat", 2019, 6.6)
car5 = Car("Volkswagen", "Bugatti Automobiles", 2015, 10.1)

lorry = Lorry("Ford", "Transit", 2021, 9.0, 2500)
sports_car = SportsCar("Ferrari", "458 Italia", 2020, 12.5, 205, 250000)

