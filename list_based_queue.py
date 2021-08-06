

class ListQueue:
    def __init__(self) -> None:
        self.items = []
        self.size = 0

    def enqueue(self, data) -> None:
        self.items.insert(0, data)
        self.size += 1

    def dequeue(self) -> any:
        data = self.items.pop()
        self.size -= 1
        return data

    def traverse(self):
        for i in range(self.size):
            print(self.items[i])

