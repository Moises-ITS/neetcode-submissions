class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        c = self.root
        for let in word:
            if let not in c.children:
                c.children[let] = TrieNode()
            c = c.children[let]
        c.word = True  

    def search(self, word: str) -> bool:
        def dfs(j, root):
            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for child in root.children.values():

                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if c not in root.children:
                        return False
                    root = root.children[c]
            return root.word
        return dfs(0, self.root)


