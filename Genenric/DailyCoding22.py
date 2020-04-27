class Solution:
    def findWordList(self, input, wordBanks):
        words = set(wordBanks)
        wordLen = len(input)

        def findword(startIdx):
            for i in range(startIdx, wordLen):
                if input[startIdx:i+1] in words:
                    #print(input[startIdx:i+1])
                    if i == wordLen - 1:
                        return [input[startIdx:i+1]]
                    temp = findword(i+1)
                    if len(temp) > 0:
                        return [input[startIdx:i+1]] + temp
            return []

        return findword(0)

if __name__ == '__main__':
    A = Solution()
    wordBanks = ["test", "heavenhell", "heaven", "chaos", "order"]
    input = "chaosheavenhelltestorder"
    print(A.findWordList(input, wordBanks))
