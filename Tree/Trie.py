class TrieNode:
    def __init__(self, char:str):
        self.char = char
        self.children = {}
        self.word_finished = False
        self.counter = 1

class Trie:
    def __init__(self):
        self.root = TrieNode('*')

    def add(self, word):
        node = self.root
        for char in word:
            if char in node.children:
                node.counter += 1
                node = node.children[char]
            else:
                node.children[char] = TrieNode(char)
                node.counter += 1
                node = node.children[char]
        node.word_finished = True


    def find_prefix(self, prefix:str):
        """
        :param prefix: the prefix of word to look for
        :return: if prefix exist return TrieNode at the end, else return None
        """
        node = self.root
        for char in prefix:
            if char not in node.children:
                return None
            node = node.children[char]
        return node

def printTrie(root:TrieNode, prefix=""):
    if root.word_finished:
        print(prefix+root.char)
    for child in root.children:
        printTrie(root.children[child], prefix+root.char)

a = Trie()
a.add("dog")
a.add("dot")
a.add("doodle")
a.add("damn")
b = a.find_prefix("da")
c = a.find_prefix("do")
printTrie(a.root)
