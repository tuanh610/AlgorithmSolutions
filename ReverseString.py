class Solution:
    def reverse(self, a:str):
        return "".join(a[::-1])

a = Solution()
print(a.reverse("Greetings!"))