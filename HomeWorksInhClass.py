class Car:
    price = 1000000
    def horse_powers(self):
        print('Двигатель', self.power, 'л.с.')


class Nissan(Car):
    price = 1500000
    power = 90

class Kia(Car):
    price = 900000
    power = 110



print('Nissan')
my_car = Nissan()
my_car.horse_powers()
print(my_car.price)

print('KIA')
my_car = Kia()
my_car.horse_powers()
print(my_car.price)