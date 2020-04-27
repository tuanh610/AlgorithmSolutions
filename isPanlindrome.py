class Solution:
    def isPalindrome(self, a:str):
        lim = len(a)//2
        for i in range(lim):
            if a[i] != a[-i-1]:
                return False
        return True

a = Solution()
print(a.isPalindrome("abcdefdg"))
print(a.isPalindrome("abcdedcba"))
print(a.isPalindrome("aba"))