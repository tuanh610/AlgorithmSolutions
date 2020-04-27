class Node:
    def __init__(self, children, isWord):
        self.children = children
        self.isWord = isWord

class Solution:
    def __init__(self):
        self.trie = None

    def buildTrie(self, words):
        self.trie = Node({}, False)
        for word in words:
            currentTrie = self.trie
            for char in word:
                if char not in currentTrie.children:
                    currentTrie.children[char] = Node({},False)
                currentTrie = currentTrie.children[char]
            currentTrie.isWord = True
        return self.trie

    def autocomplete(self, words, target):
        self.buildTrie(words)
        currentTrie = self.trie
        for char in target:
            if char not in currentTrie.children:
                return []
            currentTrie = currentTrie.children[char]
        return self.getallWordsFromTrie(currentTrie, target)

    def getallWordsFromTrie(self, trie, prefix):
        result = []
        if trie.isWord:
            result.append(prefix)
        for char in trie.children:
            result += self.getallWordsFromTrie(trie.children[char], prefix+char)
        return result

words = ['dog', 'door', 'dark', 'cat', 'doodle', 'dance', 'donkey']
target = 'do'
a = Solution()
print(a.autocomplete(words, target))
#Exptect answers: ['dog', 'door', 'doodle']