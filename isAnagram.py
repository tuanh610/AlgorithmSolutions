class Solution:
    def isAnagram(self, str1, str2):
        #process the str1 first
        str1 = str1.lower()
        str2 = str2.lower()
        def countChar(a:str):
            res = {}
            for char in a:
                if char.isalnum():
                    res[char] = res.get(char, 0) + 1
            return res
        data1 = countChar(str1)
        data2 = countChar(str2)
        if len(data1) != len(data2):
            return False
        for char in data1:
            if char not in data2 or data1[char] != data2[char]:
                return False
        return True

def BSF(start, target):
    queue = [(start, 0)]
    while len(queue) > 0:
        curNode, curLvl = queue.pop(0)
        if curNode == target:
            return curLvl
        else:
            for neighbor in curLvl.neighbors:
                queue.append((neighbor,curLvl+1))
    return curLvl

a = Solution()
print(a.isAnagram("rail safety", "fairy tales"))
print(a.isAnagram("RAIL! SAFETY!", "fairy tales"))
print(a.isAnagram("Hi there", "Bye there"))