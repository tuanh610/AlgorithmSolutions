class Solution:
    def decode(self, A):
        data = {}
        for i in range(1, 27):
            data[str(i)] = chr(ord('a') + i - 1)

        cache = {}
        def getStr(input):
            if len(input) == 1:
                return [data[input]]

            if input in cache:
                return cache[input]

            if len(input) == 2:
                temp = [data[input[0]]+data[input[1]]]
                if input in data:
                    temp.append(data[input])
                cache[input] = temp
                return temp
            else:
                temp = [data[input[0]] + x for x in getStr(input[1:])]
                if input[:2] in data:
                    temp += [data[input[:2]] + x for x in getStr(input[2:])]
                cache[input] = temp
                return temp

        res = getStr(A)
        return res

if __name__ == '__main__':
    a = Solution()
    b = '14231'
    print(a.decode(b))