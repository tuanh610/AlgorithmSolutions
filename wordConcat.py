class Solutions:
     def findConcatItems(self, words):
        wordSet = set(words)
        res = {}
        processed = {}
        for word in words:
            temp = self.findConcat(wordSet, word, processed, False)
            if len(temp) > 0:
                res[word] = temp
        return res

     def findConcat(self, wordSet, target, processed, acceptItSelf):
        res = []
        if acceptItSelf and target in wordSet:
            res.append(target)

        for i in range(1, len(target)-1):
            left = target[:i]
            right = target[i:]
            if left not in processed:
                self.findConcat(wordSet, left, processed, True)
            if right not in processed:
                self.findConcat(wordSet, right, processed, True)
            if left in processed and right in processed and len(processed[left]) > 0 and len(processed[right]) > 0:
                for leftItem in processed[left]:
                    for rightItem in processed[right]:
                        res.append(leftItem+','+rightItem)
        processed[target] = res
        return res

words = ["caats", "a", "ts", "c"]
a = Solutions()
b = a.findConcatItems(words)
print(b)