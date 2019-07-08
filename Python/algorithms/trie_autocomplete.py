class TrieNode:
    def __init__(self):
        self.children = dict()
        self.end = False

    def insert(self, char: str):
        if self.children.get(char) is None:
            self.children[char] = TrieNode()

    def suffixes(self, suffix='', words=[]) -> list:
        for letter in self.children.keys():
            current_node = self.children[letter]
            current_node.suffixes(suffix + letter, words)

        if self.end:
            words.append(suffix)
            suffix = ''
            return

        return words


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        current_node = self.root
        for letter in word:
            current_node.insert(letter)
            next_node = current_node.children.get(letter)
            current_node = next_node
        current_node.end = True

    def find(self, prefix: str) -> TrieNode:
        current_node = self.root
        for letter in prefix:
            if current_node.children.get(letter) is None:
                return False
            next_node = current_node.children.get(letter)
            current_node = next_node
        return current_node


words = [
    "trigonometry", "tripod", "trident", "trilogy",
    "tricycle", "trinity"
]

trie = Trie()

for key in words:
    trie.insert(key)


prefix = "tri"
prefix_node = trie.find(prefix)
print(prefix_node.suffixes())
