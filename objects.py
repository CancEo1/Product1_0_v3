# Purpose: Objects module to interact with Product objects.
from dataclasses import dataclass

@dataclass
class Product:
    name:str = ""
    price:float = 0.0
    discountPercent:float = 0

    def getDiscountAmount(self):
        return self.price * self.discountPercent / 100

    def getDiscountPrice(self):
        return self.price - self.getDiscountAmount()

product = Product(name="Widget", price=19.99, discountPercent=10)
product2 = Product(name="Gadget", price=29.99, discountPercent=15)
product3 = Product(name="Doodad", price=39.99, discountPercent=20)