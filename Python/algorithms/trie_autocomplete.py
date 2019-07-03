class TrieNode:
    def __init__(self):
        self.children = dict()
        self.end = False
    
    def insert(self, char: str):
        if self.children.get(char) is None:
            self.children[char] = TrieNode()
    
    def suffixes(self, suffix='', word='', words=[]) -> list:
        if suffix:
            self = self.children.get(suffix)
        
        for letter in self.children.keys():
            self.suffixes(letter, word + letter, words)

        if self.end and word:
            words.append(word)
        
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
    "ant", "anthology", "antagonist", "antonym",
    "fun", "function", "factory",
    "trie", "trigger", "trigonometry", "tripod"
]

trie = Trie()

for key in words:
    trie.insert(key)


def suggestions(prefix: str):
    prefix_node = trie.find(prefix)
    if prefix_node:
        return prefix_node.suffixes()
    else:
        return f"{prefix} not found"


print(suggestions("tri"))
print(suggestions("ant"))
print(suggestions("f"))