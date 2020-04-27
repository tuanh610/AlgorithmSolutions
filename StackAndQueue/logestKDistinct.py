from QueueImplementation import LinklistQueue

class Solution:
    def finsKDistinct(self, K, input):
        distinct = {}
        queue = LinklistQueue()
        maxL = 0
        for char in input:
            if char not in distinct:
                if len(distinct) >= K:
                    maxL = max(maxL, len(queue))
                    to_remove = queue.dequeue()
                    counter = distinct[to_remove] - 1
                    while counter > 0:
                        temp = queue.dequeue()
                        if temp == to_remove:
                            counter -= 1

                    del distinct[to_remove]
            distinct[char] = distinct.get(char, 0) + 1
            queue.enqueue(char)
        return maxL


if __name__ == '__main__':
    A = Solution()
    input = "abcbag"
    print(A.finsKDistinct(2, input))
