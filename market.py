# coding: utf-8


class PriceRules:
    """
    This class hold the rules for calculating the price of an item
    """
    def __init__(self):
        self.rules = {}

    def add(self, item, price, quantity):
        self.rules[str(item*quantity)] = price


class Checkout:
    """
    This class is responsible for scanning items and calculating the total price
    """
    def __init__(self, rules):
        self.items = []
        self.rules = rules

    def scan(self, item):
        self.items.append(item)

    def total(self):
        total = 0
        item_list = "".join(sorted(self.items))
        for item, price in self.rules:
            if item in item_list:
                count = item_list.count(item)
                total += (count * price)
                item_list = item_list.replace(item, '')

        return total
