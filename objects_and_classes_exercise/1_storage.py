class Storage:
    storage = []

    def __init__(self, capacity: int):
        self.capacity = capacity

    def add_product(self, product):
        if self.capacity > 0:
            self.capacity -= 1
            Storage.storage.append(product)

    def get_products(self):
        return Storage.storage