class BinaryTree:
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        if self.leftChild is None:
            self.leftChild = newNode
        else:
            temp = BinaryTree(newNode)
            temp.leftChild = self.leftChild
            self.leftChild = temp

    def insertRight(self, newNode):
        if self.rightChild is None:
            self.rightChild = newNode
        else:
            temp = newNode
            temp.rightChild = self.rightChild
            self.rightChild = temp

    def getLeftChild(self):
        return self.leftChild

    def getRightChild(self):
        return self.rightChild

    def setRootVal(self, obj):
        self.key = obj

    def getRootVal(self):
        return self.key

    def preOrder(self):
        print(self.key, end=' ')
        if self.leftChild:
            self.leftChild.preOrder()
        if self.rightChild:
            self.rightChild.preOrder()

    def inOrder(self):
        if not self.key:
            return
        if self.leftChild:
            self.leftChild.inOrder()
        print(self.key, end=' ')
        if self.rightChild:
            self.rightChild.inOrder()

    def postOrder(self):
        if not self.key:
            return
        if self.leftChild:
            self.leftChild.postOrder()
        if self.rightChild:
            self.rightChild.postOrder()
        print(self.key, end=' ')


tree1 = BinaryTree(5)
tree2 = BinaryTree(100)
tree3 = BinaryTree(2)
tree4 = BinaryTree(66)
tree5 = BinaryTree(1)

tree4.insertLeft(tree5)
tree2.insertRight(tree4)
tree1.insertLeft(tree2)
tree1.insertRight(tree3)

tree1.preOrder()
print("\n")
tree1.inOrder()
print("\n")
tree1.postOrder()
print("\n")
