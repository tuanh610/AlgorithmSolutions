class Solution:
    def findKLargest(self, numbers, k):
        return self.quicksort(numbers, 0, len(numbers)-1, k)

    def quicksort(self, numbers, low, high, k):
        if low < high:
            pi = self.partition(numbers, low, high)
            if pi == len(numbers) - k:
                return numbers[pi]
            elif pi < len(numbers) - k:
                return self.quicksort(numbers, pi+1, high, k)
            else:
                return self.quicksort(numbers, low, pi-1, k)
        else:
            return numbers[len(numbers)-k]

    def partition(self, numbers, low, high):
        pivot = numbers[high]
        i = low - 1
        for j in range(low, high):
            if numbers[j] < pivot:
                i += 1
                numbers[i], numbers[j] = numbers[j], numbers[i]
        numbers[i+1], numbers[high] = numbers[high], numbers[i+1]
        #print(i+1)
        #print(numbers)
        return i+1


numbers = [5, 2, 7, 3, 1, 6, 4]
k = 5
a = Solution()
print(a.findKLargest(numbers, k))
