from typing import TypeVar, Generic, Optional

T = TypeVar('T')


class TwoWayNode(Generic[T]):

    def __init__(self, data=None, next=None, previous=None) -> None:
        self.data = data
        self.next = next
        self.previos = previous


class Queue:

    head: TwoWayNode
    tail: TwoWayNode
    count: int

    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.count = None

    def enqueue(self, data) -> None:
        new_node = TwoWayNode(data, None, None)

        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.previos = self.tail
            self.tail.next = new_node
            self.tail = new_node

        self.count += 1

    def dequeue(self) -> TwoWayNode:
        current = self.head

        if self.count == 1:
            self.count -= 1
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.previos = None
            self.count -= 1

        return current
