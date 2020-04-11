class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, data):
        hashValue = self.hashfunction(key, len(self.slots))
        if self.slots[hashValue] is None:
            self.slots[hashValue] = key
            self.data[hashValue] = data
        else:
            if self.slots[hashValue] == key:
                # 替换
                self.data[hashValue] = data
            else:
                nextSlot = self.rehash(hashValue, len(self.slots))
                while (self.slots[nextSlot] is not None) and \
                        self.data[hashValue] != key:
                    nextSlot = self.rehash(nextSlot, len(self.slots))
                if self.slots[nextSlot] is None:
                    self.slots[nextSlot] = key
                    self.data[nextSlot] = data
                else:
                    # 替换
                    self.data[nextSlot] = data

    def hashfunction(self, key, size):
        return key % size

    def rehash(self, oldHash, size):
        return (oldHash+1) % size

    def get(self, key):
        startSlot = self.hashfunction(key, len(self.slots))
        data = None
        stop = False
        found = False
        position = startSlot
        while (self.slots[position] is not None) and (not found) and (not stop):
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots))
                if position == startSlot:
                    stop = True
        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)


h = HashTable()
h.put(54, "Kit")
h.put(26, "Sam")
h.put(93, "Timmy")
h.put(17, "Elan")
h[77] = "WangGang"
h.put(31, "Job")
h[44] = "Bob"
h[55] = "Dan"
h[20] = "LiHua"

print(h.get(31))
print(h.get(26))
print(h[44])
print(h[17])
