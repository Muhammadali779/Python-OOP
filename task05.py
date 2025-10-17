class Product:
    def __init__(self, name, price, category, in_stock):
        self.name = name
        self.price = price
        self.category = category
        self.in_stock = in_stock

product1 = Product("iPhone 17 Pro Max", 17_000_000.00, "electronics", True)
product2 = Product("Air Pods", 170_000.00, "electronics", False)

print(f"Maxsulot nomi: {product1.name} || Narxi: {product1.price:,.2f}")
print(f"Maxsulot nomi: {product2.name} || Narxi: {product2.price:,.2f}")