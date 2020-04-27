class MinHeap:
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.size = 0
        self.Heap = [0]*(self.maxSize+1)
        self.Heap[0] = -float('inf')
        self.Front = 1

    def parent(self, pos):
        return pos//2

    def rightChild(self, pos):
        return (2*pos+1)

    def leftChild(self, pos):
        return 2*pos

    def isLeaf(self, pos):
        if pos >= self.size // 2 and pos <= self.size:
            return True
        else:
            return False

    def swap(self,fpos, spos):
        self.Heap[fpos], self.Heap[spos] = self.Heap[spos], self.Heap[fpos]

    def minHeapify(self, pos):
        if not self.isLeaf(pos):
            if self.Heap[pos] > self.Heap[self.leftChild(pos)] or self.Heap[pos] > self.Heap[self.rightChild(pos)]:
                #swap the node
                if self.Heap[self.leftChild(pos)] < self.Heap[self.rightChild(pos)]:
                    self.swap(pos, self.leftChild(pos))
                    self.minHeapify(self.leftChild(pos))
                else:
                    self.swap(pos, self.rightChild(pos))
                    self.minHeapify(self.rightChild(pos))

    def insert(self, val):
        if self.size >= self.maxSize:
            return
        self.size += 1
        self.Heap[self.size] = val
        current = self.size
        while self.Heap[current] < self.Heap[self.parent(current)]:
            self.swap(current, self.parent(current))
            current = self.parent(current)

    def Print(self):
        for i in range(1, (self.size//2)+1):
            print("PARENT: {}-LEFT: {}-RIGHT: {}".format(self.Heap[i], self.Heap[self.leftChild(i)], self.Heap[self.rightChild(i)]))

    def minHeap(self):
        for pos in range(self.size//2, 0, -1):
            self.minHeapify(pos)

    def extractMin(self):
        popped = self.Heap[self.Front]
        self.Heap[self.Front] = self.Heap[self.size]
        self.size -= 1
        self.minHeapify(self.Front)
        return popped

print('The minHeap is ')
minHeap = MinHeap(15)
minHeap.insert(5)
minHeap.insert(3)
minHeap.insert(17)
minHeap.insert(10)
minHeap.insert(84)
minHeap.insert(19)
minHeap.insert(6)
minHeap.insert(22)
minHeap.insert(9)
minHeap.Print()
print("The Min val is " + str(minHeap.extractMin()))
print("The Min val is " + str(minHeap.extractMin()))
print("The Min val is " + str(minHeap.extractMin()))
print("The Min val is " + str(minHeap.extractMin()))
minHeap.Print()