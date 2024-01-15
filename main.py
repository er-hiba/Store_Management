from classes import Product, Store

product1 = Product("Laptop", 800, 1200, "High-performance laptop")
product2 = Product("Phone", 300, 500, "Smartphone with advanced features")
    
store = Store("Main Street", [product1, product2])

print("Initial Store:")
print(store)

store.buy_product("Laptop", 2)
store.sell_product("Phone", 1)

print("\nUpdated Store Bilan:")
print(store)
