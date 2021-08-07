

class Queue:
    def __init__(self) -> None:
        self.inbound_stack = []
        self.outbound_stack = []

    def enqueue(self, data) -> None:
        self.inbound_stack.append(data)

    def dequeue(self) -> any:
        if not self.outbound_stack:
            while self.inbound_stack:
                self.outbound_stack.append(self.inbound_stack.pop())

        return self.outbound_stack.pop()
