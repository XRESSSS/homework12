class Car:
    def __init__(self, producer, brand, year_of_release=2020, fuel_consumption: float = 0.0):
        self.producer = producer
        self.brand = brand
        self.year_of_release = year_of_release
        self.fuel_consumption = fuel_consumption
        self.run = 0

    def __str__(self):
        return f'Car {self.brand}'

    __repr__ = __str__


car = Car("Toyota", "Camry", 2022,  7.5)
сar2 = Car("Honda", "Civic", 2021,  6.8)
сar3 = Car("Volkswagen", "Phaeton", 2023,  9.1)
сar4 = Car("Volkswagen", "Passat", 2019,  6.6)
сar5 = Car("Volkswagen", "Bugatti Automobiles", 2015,  10.1)
