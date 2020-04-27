class Node:
    def __init__(self, val):
        self.val = val
        self.next, self.prev = None, None

    def __str__(self):
        return str(self.val)

class DoubleLinkList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insertLast(self, val):
        temp = Node(val)
        if self.head is None:
            self.head = temp
            self.tail = temp
        else:
            self.tail.next = temp
            temp.prev = self.tail
            self.tail = temp
        self.size += 1

    def insertAt(self, val, index):
        if index >= self.size:
            raise IndexError
        if index == self.size-1:
            return self.insertLast(val)
        temp = Node(val)
        left = self.head
        for i in range(index):
            left = left.next
        right = left.next
        left.next = temp
        temp.prev = left
        right.prev = temp
        temp.next = right
        self.size += 1

    def removeLast(self):
        if self.tail is None:
            raise ValueError

        self.tail = self.tail.prev
        self.size -= 1

        if self.tail is None:
            self.head = None
        else:
            self.tail.next = None

    def removeAt(self, index):
        if index >= self.size:
            raise IndexError
        if index == 0:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
        elif index == self.size-1:
            return self.removeLast()
        else:
            cur = self.head
            for i in range(index):
                cur = cur.next
            left, right = cur.prev, cur.next
            left.next, right.prev = right, left


    def printLL(self):
        cur = self.head
        res = ""
        while cur is not None:
            res += str(cur.val) + "-"
            cur = cur.next
        print(res[:-1])

if __name__ == "__main__":
    A = DoubleLinkList()
    A.insertLast(10)
    A.insertLast(5)
    A.insertLast(3)
    A.printLL()
    A.insertAt(6,1)
    A.printLL()
    A.removeLast()
    A.printLL()
    A.insertAt(3, 0)
    A.printLL()
    A.removeAt(2)
    A.printLL()