class DicNode:
    def __init__(self):
        self.isWord = False
        self.children = {}

class WordDictionary:

    def __init__(self):
        self.root = DicNode()

    def addWord(self, word: str) -> None:
        path = self.root
        for letter in word:
            if letter not in path.children:
                path.children[letter] = DicNode()
            path = path.children[letter]
        path.isWord = True

    def search(self, word: str) -> bool:
        # look down the path
        # when there is a dot call the function on all paths in curr path
        def dfs(j, curr):
            for i in range(j, len(word)):
                if word[i] == ".":
                    for node in curr.children.values():
                        return dfs(i + 1, node)
                if word[i] not in curr.children:
                    return False
                else:
                    curr = curr.children[word[i]]
            return curr.isWord
        curr = self.root
        return dfs(0, curr)
        