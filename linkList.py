class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __str__(self):
        return str(self.val)

class LinkList:
    def __init__(self):
        self.head = None
    def getAt(self, idx):
        if self.head is None or idx < 0:
            raise IndexError
        counter = 0
        cur = self.head
        while counter < idx:
            cur = cur.next
            counter += 1
            if cur is None:
                raise IndexError
        return cur

    def getSize(self):
        cur = self.head
        res = 0
        while cur is not None:
            res += 1
            cur = cur.next
        return res

    def clear(self):
        self.head = None

    def insertAt(self, val, idx):
        if idx == 0:
            temp = Node(val)
            temp.next = self.head
            self.head = temp
            return
        try:
            tempNode = self.getAt(idx)
            temp = Node(val)
            temp.next = tempNode.next
            tempNode.next = temp
        except IndexError:
            print("Index out of bound")

    def removeAt(self, idx):
        if self.head is None:
            print("Index out of bound")
            return
        if idx == 0:
            self.head = self.head.next
            return
        try:
            parentNode = self.getAt(idx-1)
            if parentNode.next is None:
                raise IndexError
            parentNode.next = parentNode.next.next
        except IndexError:
            print("Index out of bound")

    def removeFirst(self):
        self.removeAt(0)

    def insertFirst(self):
        self.insertAt(0)

    def insertLast(self, val):
        if self.head is None:
            self.head = Node(val)
            return
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(val)

    def removeLast(self):
        if self.head is None:
            raise IndexError
        if self.head.next is None:
            self.head = None
            return
        cur = self.head
        while cur.next is not None:
            if cur.next.next is None:
                cur.next = None
                return
            cur = cur.next

    def printList(self):
        cur = self.head
        res = ""
        while cur is not None:
            res += str(cur.val) + "-"
            cur = cur.next
        print(res[:-1])

    def getMid(self):
        if self.head is None:
            return None
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            if fast is not None:
                slow = slow.next
        return slow

if __name__ == '__main__':
    a = LinkList()
    a.insertLast(5)
    a.insertLast(10)
    a.insertLast(15)
    a.insertLast(20)
    a.insertLast(25)
    #a.insertLast(30)
    print(a.getMid().val)