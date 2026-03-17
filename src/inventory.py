class Inventory:
    def __init__(self, items=None):
        self.items = items if items is not None else {}

    def add_item(self, item, quantity):
        if item.name in self.items:
            self.items[item.name] += item.quantity
        else:
            self.items[item.name] = item.quantity

    def remove_item(self, item):
        if item.name in self.items:
            del self.items[item.name]
