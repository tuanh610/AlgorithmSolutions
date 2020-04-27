class Solution:
    def fizzBuzz(self, n):
        for i in range(1, n+1):
            if i%15 == 0:
                print("fizzbuzz")
            elif i%5 == 0:
                print("buzz")
            elif i%3 == 0:
                print("fizz")
            else:
                print(i)

a = Solution()
a.fizzBuzz(15)