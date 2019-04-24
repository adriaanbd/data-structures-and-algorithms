from unittest import TestCase
from ..node import Node

class TestNode(TestCase):
    def test_node_init(self):
        n = Node(1)
        self.assertIsInstance(n, Node)

    def test_node_data(self):
        n = Node(1)
        self.assertEqual(1, n.key)

    def test_node_next_pointer(self):
        n1 = Node(1)
        n2 = Node(2)
        n1.next_pointer = n2
        self.assertEqual(n1.next_pointer, n2)

    def test_is_node_next_pointer_data_next_pointer_node(self):
        n1 = Node(1)
        n2 = Node(2)
        n1.next_pointer = n2
        self.assertTrue(n1.next_pointer.key == n2.key)
