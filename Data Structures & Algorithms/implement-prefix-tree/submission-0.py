class TreeNode:
    def __init__(self):
        self.isWord = False
        self.letters = {}

class PrefixTree:

    def __init__(self):
        self.root = TreeNode()

    def insert(self, word: str) -> None:
        path = self.root
        for letter in word:
            # check if it is in the tree
            if letter not in path.letters:
                path.letters[letter] = TreeNode()
            path = path.letters[letter]
        path.isWord = True

    def search(self, word: str) -> bool:
        path = self.root
        for letter in word:
            if letter in path.letters:
                path = path.letters[letter]
            else:
                return False
        return path.isWord

    def startsWith(self, prefix: str) -> bool:
        path = self.root
        for letter in prefix:
            if letter in path.letters:
                path = path.letters[letter]
            else:
                return False
        return True

        