from random import sample

class Solution:
    def generateRandom(self):
        res = []
        vowels = ["a", "i", "u", "e", "o"]
        consonents = ["", "k", "s"]
        for v in vowels:
            for c in consonents:
                res.append(c+v)
        return sample(res, len(res))

if __name__ == '__main__':
    A = Solution()
    print(A.generateRandom())