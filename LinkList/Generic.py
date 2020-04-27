from random import randint
from random import seed
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __str__(self):
        return str(self.val)

class GenerateLL:
    def __init__(self, n):
        #seed(6)
        if n < 1:
            raise IndexError
        self.head = Node(randint(0,9))
        cur = self.head
        for i in range(1,n):
            next = Node(randint(0, 9))
            cur.next = next
            cur = next


def printLL(head):
    cur = head
    res = ""
    while cur is not None:
        res += "{}-".format(str(cur.val))
        cur = cur.next
    print(res[:-1])
