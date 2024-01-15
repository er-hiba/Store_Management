class Product:   
    def __init__(self, name, purchase_price, selling_price, description = "No Description", quantity = 0):
        self.__name = name
        self.__purchase_price = purchase_price
        self.__selling_price = selling_price
        self.__description = description
        self.__quantity = quantity

    @property
    def get_name(self):
        return self.__name

    @property
    def get_purchase_price(self):
        return self.__purchase_price

    @property
    def get_selling_price(self):
        return self.__selling_price

    @property 
    def get_description(self):
        return self.__description

    @property
    def get_quantity(self):
        return self.__quantity

    def set_quantity(self, new_q):
        self.__quantity = new_q
    
    def set_description(self, new_d):
        self.__description = new_d

    def __str__(self):
        return f"{self.__name}, {self.__purchase_price}, {self.__selling_price}, {self.__description}, {self.__quantity}"

class Store:
    def __init__(self, address, stock):
        self.__address = address
        self.__stock = stock.copy()

    @property
    def get_adr(self):
        return self.__address

    @property
    def get_stock(self):
        return self.__stock

    def set_adr(self, new_adr):
        self.__address = new_adr

    def set_stock(self, new_s):
        self.__stock = new_s

    def add_product(self, product):
        self.__stock.append(product)

    def buy_product(self, name, quantity):
        for x in self.__stock:
            if name == x.get_name:
                x.set_quantity(x.get_quantity + quantity)
                print(f"Bought {quantity} {name}(s).")
                return
        print(f"{name} not found in stock. Unable to complete purchase.")

    def sell_product(self, name, quantity):
        for x in self.__stock:
            if name == x.get_name:
                if x.get_quantity >= quantity:
                    x.set_quantity(x.get_quantity - quantity)
                    print(f"Sold {quantity} {name}(s).")
                    return
                else:
                    print(f"Insufficient stock for {name}. Unable to complete sale.")
                    return
        print(f"{name} not found in stock. Unable to complete sale.")

    def __str__(self):
        product_info = [f"{product.get_name}: Quantity={product.get_quantity}, Price={product.get_selling_price}" for product in self.__stock ]
        return f"Address: {self.__address} \nProducts:\n" + "\n".join(product_info)
