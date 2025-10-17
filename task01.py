class Car:
    def __init__(self, brand, model, year):
        self.brendi = brand
        self.modeli = model
        self.yili = year


car1 = Car("BMW", "BMW M5 Competition", 2024)
car2 = Car("BMW", "BMW M4 Competition", 2022)
car3 = Car("Mecedes-Benz", "GT 63 S", 2020)
car4 = Car("AUDI", "RS 7", 2021)

cars = [car1, car2, car3, car4]

for car in cars:
    print(f"{car.modeli} -> {car.yili} - yilda ishlab chiqarilgan, Brendi: {car.brendi}")