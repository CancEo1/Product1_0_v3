# Purpose: Product Viewer_1.0 use objects created from a Product class.
# Begin by displaying a numbered list of 3 products. The can view data for a product by entering the number
# Code for the Product class is stored in a file named objects.py
# show_products() function displays a numbered list of products.
## Important things to remember: This will help with Project3
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

from objects import Product

def show_products(products):
    print("Products")
    for i, product in enumerate(products, start=1):
        print(f"{i}.{product.name}")
    print(products)

def show_product(product):
    w = 18  
    print(f"{'Name:':{w}}{product.name}")
    print(f"{'Price:':{w}}${product.price:.2f}")
    print(f"{'Discount Percent:':{w}}{product.discountPercent:d}%")
    print(f"{'Discount Amount:':{w}}${product.getDiscountAmount():.2f}")
    print(f"{'Discount Price:':{w}}${product.getDiscountPrice():.2f}")
    print()

def get_products():
    # return a tuple of Product objects
    return (Product(name="Widget", price=19.99, discountPercent=10),
            Product(name="Gadget", price=29.99, discountPercent=15),
            Product(name="Doodad", price=39.99, discountPercent=20))

def get_product(products):
    while True:
        try:
            number = int(input("Enter product number: "))
            if number < 1 or number > len(products):
                print("Product number out of range. Please try agian.")
            else:
                return products[number-1] # if the number is valid return the products
        except ValueError:
            print("Invalid number. Please try again.") # Catching ValueError's to avoid crash
        print()

def main():
    print("The Product Viewer program")
    print()

    products = get_products()
    show_products(products)

    choice = "y"
    while choice.lower() == "y":
        product = get_product(products)
        show_product(product)

        choice = input("View another product? (y/n): ")
        print()
    print("Goodbye!")

if __name__ == "__main__":
    main()