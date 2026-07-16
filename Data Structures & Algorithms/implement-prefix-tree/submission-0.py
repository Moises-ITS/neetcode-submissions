class PrefixTree:

    def __init__(self):
        self.lis = set()

    def insert(self, word: str) -> None:
        if word not in self.lis:
            self.lis.add(word)
        else:
            print("Already inserted")

    def search(self, word: str) -> bool:
        for words in self.lis:
            if words == word:
                return True
        return False

    def startsWith(self, prefix: str) -> bool:
        for words in self.lis:
            if words.startswith(prefix):
                return True
        return False
        