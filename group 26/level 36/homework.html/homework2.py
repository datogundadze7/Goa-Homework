# Dictionary of products with their availability status
products = {
    " apples": True,
    "bananas": False,
    "oranges": True,
    "grapes": False,
    "pears": True
}

# Use filter to get only products that are not in stock (False)
out_of_stock = dict(filter(lambda item: not item[1], products.items()))

# Print the result
print("Products that are out of stock:", out_of_stock)

