class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)


class StackLower:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.insert(0, item)

    def pop(self):
        return self.item.pop(0)

    def peek(self):
        return self.items[0]

    def size(self):
        return len(self.items)


s = Stack()
print(s.isEmpty())
s.push('Hello')
s.push(101)
s.push(3.14)
print(s.peek())
s.push(False)
s.push([])
print(s.size())
print(s.isEmpty())
s.push({1, 2})
print(s.pop())
print(s.size())
