# Create a Python dictionary to represent a simple product catalog. The dictionary should contain three products, with each product's SKU (Stock Keeping Unit) serving as the key. Include the following information as values for each product:
# name: The name of the product.
# price: The price of the product.
# quantity: The number of items in stock.

product_catalog = {
	"SKU123": {"name": "Widget A", "price": 19.99, "quantity": 50},
	"SKU456": {"name": "Gadget B", "price": 34.95, "quantity": 25},
	"SKU789": {"name": "Gizmo C", "price": 9.99, "quantity": 100}
}
print("Write the SKU key of the product you want to find:")
sku_to_find = input("SKU: ")
if sku_to_find not in product_catalog:
    print(f"Product with SKU {sku_to_find} not found.")
else:
	print(f"The price of {product_catalog[sku_to_find]['name']} is {product_catalog[sku_to_find]['price']}")