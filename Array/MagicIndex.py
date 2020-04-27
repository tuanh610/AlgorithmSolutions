from random import randint

class Solution:
    def magicIndexNoDuplicate(self, arr):
        def find(start, end):
            if end < start:
                return None
            mid = start + (end-start)//2
            if arr[mid] == mid:
                return mid
            elif arr[mid] > mid:
                return find(start,mid-1)
            else:
                return find(mid+1, end)
        return find(0, len(arr)-1)

    def magicIndexWithDuplicate(self, arr):
        def find(start, end):
            if end < start:
                return None
            mid = start + (end-start)//2
            if arr[mid] == mid:
                return mid
            else:
                temp = find(start, min(arr[mid], mid-1))
                if temp is None:
                    temp = find(max(arr[mid], mid+1), end)
                return temp

        return find(0, len(arr)-1)


if __name__ == '__main__':
    arr = [1,2,4,4,6,7,7,9,10]
    A = Solution()
    print(A.magicIndexWithDuplicate(arr))
