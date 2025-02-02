class Product:
    def __init__(self,name,price,stock):
        self.name=name
        self.price=price
        self.stock=stock
    def check_availability(self,quantity):
        if quantity<=self.stock:
            return True
        else:
            return False
name=input("enter the name of the product:")
price=float(input("enter the price of the product:"))
stock=int(input("enter the stock of the product:"))
quant=int(input("enter the quantity:"))
p=Product(name,price,stock)
if(p.check_availability(quant)==True):
    print("product is available")
else:
    print("Product is not available")