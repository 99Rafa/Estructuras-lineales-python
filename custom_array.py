from random import randint
from functools import reduce


class Array:
    def __init__(self, capacity, fill_value=None) -> None:
        self.capacity = capacity
        self.items = list()
        for _ in range(capacity):
            self.items.append(fill_value)

    def __len__(self) -> int:
        return len(self.items)

    def __str__(self) -> str:
        return str(self.items)

    def __iter__(self) -> iter:
        return iter(self.items)

    def __getitem__(self, index) -> any:
        return self.items[index]

    def __setitem__(self, index, new_item) -> None:
        self.items[index] = new_item

    def fill_random(self) -> None:
        self.items = [randint(0, 100) for i in range(self.capacity)]

    def summ_all(self) -> None:
        return reduce(lambda a, b: a+b, self.items)
