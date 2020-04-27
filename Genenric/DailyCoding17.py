class Solution:
    def findLongestPath(self, input):
        #split by \n
        data = input.split(r"\n")
        lvlData = []
        result = 0
        for word in data:
            #find the level
            lvl = 0
            curIdx = 0
            while curIdx < len(word) and word[curIdx:].startswith(r"\t"):
                curIdx += 2
                lvl += 1
            if curIdx == len(word) or lvl > len(lvlData):
                raise ValueError
            if lvl == 0:
                temp = len(word)
            else:
                temp = lvlData[lvl-1] + 1 + len(word) - 2*lvl
            #Check if currentwork is a file
            if word.endswith('.ext'):
                result = max(result, temp)
            if lvl == len(lvlData):
                lvlData.append(temp)
            else:
                lvlData[lvl] = temp
        return result


if __name__ == '__main__':
    #input = r"dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
    #input = r"dir\n\tsubdir1\n\t\tnofile\n\t\tsubsubdir1\n\tsubdir2\n\t\tshort2\n\t\t\tfile2.ext"
    input = r"dir\n\tsubdir1\n\t\tnofile\n\t\tsubsubdir1\n\tsubdir2\n\t\tshort2\n\t\t\tnofile2"
    A = Solution()
    print(A.findLongestPath(input))