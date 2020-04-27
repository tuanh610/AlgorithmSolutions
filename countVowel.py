class Solution:
    def countVowel(self, a):
        vowels = {'a', 'e', 'i', 'o', 'u'}
        res = 0
        for char in a.lower():
            if char in vowels:
                res+=1
        return res

a = Solution()
print(a.countVowel('Hi There!'))
print(a.countVowel('HI THerE'))