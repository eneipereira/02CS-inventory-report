from collections.abc import Iterator


class InventoryIterator(Iterator):
    def __init__(self, data):
        self.data = data
        self.curr = 0

    def __next__(self):
        product = self.data[self.curr]

        if not product:
            raise StopIteration()

        self.curr += 1

        return product
