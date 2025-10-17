class Product:
    def __init__(self, name, price, category, in_stock):
        self.name = name
        self.price = price
        self.category = category
        self.in_stock = in_stock

    def check_stock(self):
        if self.in_stock:
            print(f"{self.name} omborda mavjud ✅")
        else:
            print(f"{self.name} hozirda tugagan ❌")

product1 = Product("iPhone 17 Pro Max", 17_000_000.00, "electronics", True)
product2 = Product("Air Pods", 170_000.00, "electronics", False)

products_list = [product1, product2]

for i in products_list:
    i.check_stock()