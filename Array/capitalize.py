class Solution:
    def capitalize(self, str):
        temp = str.split(' ')
        #the short version
        def processWordSimple(word):
            res = word[0].upper()
            if len(word) > 1:
                res += word[1:]
            return res
        #the long version to negate sentence errors
        def processWord(word):
            idx = -1
            for i, char in enumerate(word):
                if char.isalnum():
                    idx = i
                    break
            if idx == -1:
                return word
            elif idx == 0:
                res = word[0].upper() + word[1:]
            elif idx == len(word)-1:
                res = word[:-1] + word[-1].upper()
            else:
                res = word[:idx] + word[idx].upper() + word[idx+1:]
            return res

        temp = map(processWord, temp)
        return " ".join(temp)

    def capitalize2(self, a):
        if a[0].isalpha():
            res = a[0].upper()
        else:
            res = a[0]
        for i in range(1,len(a)):
            if a[i-1] == ' ':
                res += a[i].upper()
            else:
                res += a[i]
        return res

a = Solution()
print(a.capitalize2("This is test1, a pen is good"))