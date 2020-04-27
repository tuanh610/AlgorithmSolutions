class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinklistQueue:
    def __init__(self):
        self.start = None
        self.end = None
        self.size = 0

    def enqueue(self, val):
        temp = Node(val)
        if self.start is None:
            self.start = temp
            self.end = temp
        else:
            self.end.next = temp
            self.end = temp
        self.size += 1

    def dequeue(self):
        if self.start is None:
            raise IndexError
        temp = self.start.val
        self.start = self.start.next
        if self.start is None:
            self.end = None
        self.size -= 1
        return temp

    def isEmpty(self):
        return True if self.start is None else False

    def peek(self):
        if self.start is None:
            raise IndexError
        return self.start.val

    def __len__(self):
        return self.size

    def __str__(self):
        cur = self.start
        res = ""
        while cur is not  None:
            res += str(cur.val) + "-"
            cur = cur.next
        return res[:-1]

class ArrayQueue():
    def __init__(self):
        self.data = []

    def enqueue(self, val):
        self.data.append(val)

    def dequeue(self):
        return self.data.pop(0)

    def isEmpty(self):
        return True if len(self.data) == 0 else False

    def peek(self):
        if len(self.data) == 0:
            raise IndexError
        return self.data[0]

    def __str__(self):
        print(self.data)

def weave(q1:LinklistQueue, q2: LinklistQueue):
    res = LinklistQueue()
    if q1.start is None:
        res.start = q2.start
        res.end = q2.end
    elif q2.start is None:
        res.start = q1.start
        res.end = q1.end
    else:
        while not q1.isEmpty() and not q2.isEmpty():
            res.enqueue(q1.dequeue())
            res.enqueue(q2.dequeue())
        if not q1.isEmpty():
            res.end.next = q1.start
            res.end = q1.end
        elif not q2.isEmpty():
            res.end.next = q2.start
            res.end = q2.end
    return res

if __name__ == '__main__':
    a = LinklistQueue()
    a.enqueue(5)
    a.enqueue(4)
    b = LinklistQueue()
    b.enqueue("hello")
    b.enqueue("there")
    b.enqueue("TuAnh")
    b.enqueue("1234")
    print(weave(a,b))