class CircularQueueTwoStacks:
    def __init__(self, capacity):
        self.in_stack = []
        self.out_stack = []
        self.capacity = capacity

    def enqueue(self, item):
        if len(self.in_stack) + len(self.out_stack) >= self.capacity:
            print("Queue is Full!")
            return
        self.in_stack.append(item)
        print(f"Enqueued: {item}")

    def dequeue(self):
        if not self.in_stack and not self.out_stack:
            print("Queue is Empty!")
            return None
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        item = self.out_stack.pop()
        print(f"Dequeued: {item}")
        return item

if __name__ == "__main__":
    q = CircularQueueTwoStacks(3)
    q.enqueue(10)
    q.enqueue(20)
    q.dequeue()
