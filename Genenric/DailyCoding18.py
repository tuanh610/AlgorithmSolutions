from linkList import LinkList

class specialLinkList(LinkList):
    def removeOutofWindow(self, lim):
        cur = self.head
        while cur is not None and cur.val <= lim:
            cur = cur.next
        self.head = cur

    def removeUnnessaryNode(self, arr, i):
        if self.head is None:
            return
        if arr[self.head.val] < arr[i]:
            self.head = None
            return
        cur = self.head
        while cur is not None:
            if cur.next is not None and arr[cur.next.val] <= arr[i]:
                cur.next = None
                break
            cur = cur.next




class Solution:
    def slidingMaxWindow(self, arr, k):
        A = specialLinkList()
        for i in range(k):
            A.removeUnnessaryNode(arr, i)
            A.insertLast(i)
            #A.printList()
        res = [arr[A.head.val]]
        for i in range(k,len(arr)):
            A.removeOutofWindow(i-k)
            A.removeUnnessaryNode(arr, i)
            A.insertLast(i)
            #A.printList()
            res.append(arr[A.head.val])
        return res

if __name__ == '__main__':
    A = Solution()
    arr = [10,5,2,7,8,7]
    print(A.slidingMaxWindow(arr, 3))