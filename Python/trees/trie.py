class TrieNode:
    def __init__(self):
        self.children = dict()
        self.end = False
    
    def insert(self, char):
        if self.children.get(char) is None:
            self.children[char] = TrieNode()
        

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current_node = self.root
        for letter in word:
            current_node.insert(letter)
            next_node = current_node.children.get(letter)
            current_node = next_node
        current_node.end = True

    def find(self, prefix):
        current_node = self.root
        for letter in prefix:
            if current_node.children.get(letter) is None:
                return False
            next_node = current_node.children.get(letter)
            current_node = next_node
        return current_node.end


keys = ["apple", "orange"]
trie = Trie()

for key in keys:
    trie.insert(key)

print(trie.find("apple") == True)
print(trie.find("orange") == True)
print(trie.find("lemon") == False)