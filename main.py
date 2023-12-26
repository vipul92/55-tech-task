# coding: utf-8
import json
from market import PriceRules, Checkout


rules = PriceRules()
rule_json = [
    {"sku": "A", "price": 50, "quantity": 1},
    {"sku": "A", "price": 130, "quantity": 3},
    {"sku": "B", "price": 30, "quantity": 1},
    {"sku": "B", "price": 45, "quantity": 2},
    {"sku": "C", "price": 20, "quantity": 1},
    {"sku": "D", "price": 15, "quantity": 1},
]
for rule in rule_json:
    rules.add(rule["sku"], rule["price"], rule["quantity"])

print("Welcome to the Market!")
print("Pricing Rules: ", json.dumps(rules.rules, indent=4))

print("Scanning items...")
pr = reversed(sorted(rules.rules.items()))
co = Checkout(pr)

while True:
    # ask the user for item SKU or finish scanning
    item = input("Enter item SKU or leave empty to finish: ")
    if not item:
        break
    co.scan(item)
price = co.total()
print("Total price: ", price)
