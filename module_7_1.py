import pprint

class Product:
    def __init__(self, name = str, weight = float, category = str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        products = file.read()
        file.close()
        return products

    def add(self, *products):
        sh_products = self.get_products()
        for i in products:
            if str(i) in sh_products:
                print(f'Продукт {i} уже есть в магазине')
            else:
                sh_products = sh_products + f'\n{i}'
        file = open(self.__file_name,'w')
        file.write(sh_products)
        file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
