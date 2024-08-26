class Product():
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        stroka = f'{self.name}, {self.weight}, {self.category}'
        return stroka

class Shop():
    __file_name = 'products.txt'
    def get_products(self):
        file = open(self.__file_name, 'r')
        products = file.read()
        return products

    def add(self, *products):
        for i in products:
            file = open(self.__file_name, 'r')
            if i.__str__() in file.read():
                    print(f'Продукт {i.__str__()} уже есть в магазине')
            else:
                file = open(self.__file_name, 'a')
                file.write(f'{i}\n')



s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())