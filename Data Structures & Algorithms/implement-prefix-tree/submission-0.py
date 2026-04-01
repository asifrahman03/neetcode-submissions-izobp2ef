class PrefixTree:

    def __init__(self):
        self.wordSet = set() # Add all inserts into this
        self.prefixes = set() # Store all inserted prefixes

    def insert(self, word: str) -> None:
        self.wordSet.add(word)
        for i in range(len(word)):
            self.prefixes.add(word[:i+1])

    def search(self, word: str) -> bool:
        if word in self.wordSet:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        if prefix in self.prefixes:
            return True
        return False
        