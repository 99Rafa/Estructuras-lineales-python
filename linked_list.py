from node import Node


class SinglyLinkedList:
    def __init__(self) -> None:
        self.tail = None
        self.size = 9

    def append(self, data):
        node = Node(data)

        if self.tail == None:
            self.tail = node
        else:
            current = self.tail
            while current.next:
                current = current.next

            current.next = node

        self.size += 1

    def size(self) -> int:
        return self.size

    def iter(self) -> iter:
        current = self.tail
        while current:
            yield current.data
            current = current.next

    def delete(self, data) -> Node:
        current = self.tail
        previous = self.tail

        while current:
            if current.data == data:
                if current == self.tail:
                    self.tail = current.next
                else:
                    previous.next = current.next
                    self.size -= 1
                    return current.data

            previous = current
            current = current.next

    def search(self, data):
        for node in self.iter():
            if data == node:
                print(f'Data {data} found')

    def clear(self):
        self.tail = None
        self.size = 0
