"""
At the basic core, it is comprised of building a Huffman tree, encoding the data, and, lastly, decoding the data.

Take a string and determine the relevant frequencies of the chars.
Build and sort a list of tuples from lowest to highest frequencies.
Build the Huffman Tree by assigning a binary code to each letter, using shorter codes for the more frequent letters.
(This is the heart of the Huffman algorithm.)
Trim the Huffman Tree (remove the frequencies from the previously built tree).
Encode the text into its compressed form.
Decode the text from its compressed form.
"""

from queue import PriorityQueue


class Node:
    def __init__(self, char=None, freq=None):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __eq__(self, other):
        return self.freq == other.freq

    def __lt__(self, other):
        return self.freq < other.freq

    def __gt__(self, other):
        return self.freq > other.freq

    def __add__(self, other):
        return self.freq + other.freq

    def __radd__(self, other):
        if other == 0 or other.freq is None:
            return self
        return self.__add__(other)

    def __repr__(self):
        return f"Char:{self.char}, Left: {self.left}, Right:{self.right}"


class HuffmanCoding:
    def __init__(self, data):
        self.root = None
        self.queue = PriorityQueue()
        self.codes = dict()
        self.data = data

    def compress(self):
        self.set_frequencies()
        self.build_tree()
        encoded_data = self.encode()
        return encoded_data

    def set_frequencies(self):
        frequencies = dict()
        for char in self.data:
            if frequencies.get(char) is not None:
                node = frequencies[char]    # get node
                node.freq += 1         # increase frequency
            else:
                node = Node(char, 1)        # make node
                frequencies[char] = node    # char to node
                self.queue.put(node)        # enqueue node

    def build_tree(self):
        while len(self.queue.queue) > 1:
            nodes = [self.queue.get(), self.queue.get()]  # get nodes with least frequencies
            parent = Node(freq=sum(nodes))  # create parent node with frequency sum
            parent.left, parent.right = nodes   # create sub tree
            self.queue.put(parent)  # reinsert back to queue
        self.root = self.queue.queue[0]

    def encode(self):
        self.path_from_node_to_root(self.root)
        message = ''
        for char in self.data:
            message += self.codes[char]
        return message

    def path_from_node_to_root(self, root, bit=None):
        if root is None:
            return

        if bit is None:
            bit = ''

        if root.char:
            self.codes[root.char] = bit
            return

        self.path_from_node_to_root(root.left, bit + '0')
        self.path_from_node_to_root(root.right, bit + '1')


def huffman_encoding(data):
    tree = HuffmanCoding(data)
    message = tree.compress()
    return message, tree.root


def huffman_decoding(data, tree):
    current = tree
    message = ''

    for bit in data:
        if not current.left and not current.right:
            message += current.char
            current = tree

        if bit == '0':
            current = current.left
        else:
            current = current.right

    message += current.char
    return message


a_great_sentence = "The bird is the word"

encoded_data, tree = huffman_encoding(a_great_sentence)
decoded_data = huffman_decoding(encoded_data, tree)

print(encoded_data, tree)
print(decoded_data)

