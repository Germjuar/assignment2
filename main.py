from inventory import Inventory


names = [
    "apples",
    "soup",
    "milk",
    "tofu",
    "poptarts",
    "lightbulbs",
    "soda",
    "chips",
]

stocks = [
    7,
    6,
    3,
    1,
    2,
    0,
    5,
    24
]

prices = [
    3.99,
    1.99,
    2.50,
    4.50,
    5.99,
    8.05,
    2.99,
    1.99
]

inventory = Inventory(names, stocks, prices)
print("==", "Here are the results of creating the Inventory")
print(inventory)

max_price = inventory.find_max_price()
print("==", "Here's' the product with the maximum price:")
print(max_price)

max_investment = inventory.find_max_investment()
print("==", "Here's the product with the maximum investment:")
print(max_investment)

inventory.sort_by_stock()
print("==", "Here are the products ordered by increasing stock-count: ")
print(inventory)
