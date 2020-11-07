class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


q = Queue()
print(q.isEmpty())
q.enqueue('Hello')
q.enqueue(101)
q.enqueue(3.14)
print(q.dequeue())
q.enqueue(False)
q.enqueue([])
print(q.size())
print(q.isEmpty())
q.enqueue({1, 2})
print(q.dequeue())
print(q.size())
