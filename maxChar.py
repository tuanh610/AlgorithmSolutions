class Solution:
    def maxChar(self, a:str):
        data = {}
        maxNumber = 0
        res = None
        for char in a:
            data[char] = data.get(char, 0) + 1
            if maxNumber < data[char]:
                maxNumber = data[char]
                res = char
        return res

a = Solution()
print(a.maxChar("apple 1231111"))