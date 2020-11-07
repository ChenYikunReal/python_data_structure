class ArrayList:
    def __init__(self):
        # 新数组大小的幂次(底数为2)
        self.sizeExponent = 0
        # 当前数组（Python列表）的大小
        self.maxSize = 0
        # 当前顺序表的末尾元素下标
        self.lastIndex = 0
        # 实际上的数组（其实是Python列表）
        self.myArray = []

    def append(self, val):
        # 选择while能够保证大规模数据插入也能不溢出，但是这里其实没必要，if足矣
        if self.lastIndex > self.maxSize-1:
            self.__resize()
        self.myArray[self.lastIndex] = val
        self.lastIndex += 1

    def __resize(self):
        newSize = 2 ** self.sizeExponent
        print("new size = ", newSize)
        newArray = [0] * newSize
        for i in range(self.maxSize):
            newArray[i] = self.myArray[i]
        self.maxSize = newSize
        self.myArray = newArray
        self.sizeExponent += 1

    def __getitem__(self, index):
        if index < self.lastIndex:
            return self.myArray[index]
        else:
            raise LookupError('index out of bounds')

    def __setitem__(self, index, value):
        if index < self.lastIndex:
            self.myArray[index] = value
        else:
            raise LookupError('index out of bounds')

    def insert(self, index, value):
        if self.lastIndex > self.maxSize - 1:
            self.__resize()
        for i in range(self.lastIndex, index-1, -1):
            self.myArray[i+1] = self.myArray[i]
        self.lastIndex += 1
        self.myArray[index] = value

    def pop(self):
        temp = self.myArray[self.lastIndex]
        self.lastIndex -= 1

    def index(self, value):
        for i in range(self.lastIndex):
            if value == self.myArray[i]:
                return i
        return None


testList = ArrayList()
testList.append(2)
testList.append(100)
testList.append(1)
print(testList.maxSize)
print(testList.sizeExponent)
print(testList.lastIndex)
testList.pop()
print(testList.lastIndex)
testList[0] = 10000
# print(testList[0])
for i in range(testList.lastIndex):
    print(testList[i])
print(testList.index(10000))
