from unittest import TestCase, main
from ..singly_linked_list import LinkedList
from ..node import Node

class TestLinkedLists(TestCase):
    def test_link_list_init(self):
        l = LinkedList()
        self.assertIsInstance(l, LinkedList)

    def test_link_list_head_and_tail_init(self):
        l = LinkedList()
        self.assertIsNone(l.head and l.tail)

    def test_link_list_size_init(self):
        l = LinkedList()
        self.assertEqual(0, l.size)

    def test_link_list_add_back_first_item(self):
        l = LinkedList()
        n = Node(2)
        l.add_back(n)
        self.assertEqual(l.size, 1)
        self.assertTrue(l.head == l.tail)
        self.assertEqual(n, l.head)

    def test_link_list_add_back_two_items(self):
        l = LinkedList()
        n1, n2 = Node(2), Node(3)
        l.add_back(n1)
        l.add_back(n2)
        n1.next_pointer = n2
        self.assertEqual(l.size, 2)
        self.assertFalse(l.head == l.tail)
        self.assertEqual(n1, l.head)
        self.assertEqual(n2, l.tail)

    def test_add_back_three_items(self):
        l = LinkedList()
        n1, n2, n3 = Node(2), Node(3), Node(4)
        l.add_back(n1)
        l.add_back(n2)
        l.add_back(n3)
        n1.next_pointer = n2
        n2.next_pointer = n3
        self.assertEqual(l.size, 3)
        self.assertFalse(l.head == l.tail)
        self.assertEqual(n1, l.head)
        self.assertEqual(n3, l.tail)

    def test_get_node_by_index(self):
        l = LinkedList()
        n1, n2, n3, n4 = Node(2), Node(3), Node(4), Node(5)
        l.add_back(n1)
        l.add_back(n2)
        l.add_back(n3)
        l.add_back(n4)
        self.assertEqual(l.get(2), 4)

    def test_get_node_raise_index_error(self):
        l = LinkedList()
        n1 = Node(1)
        l.add_back(n1)
        with self.assertRaises(IndexError):
            l.get(1)

    def test_add_to_front(self):
        l = LinkedList()
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)
        l.add_back(n1)
        l.add_front(n2)
        l.add_front(n3)
        self.assertEqual(l.head, n3)
        self.assertEqual(l.tail, n1)

if __name__ == '__main__':
    main()
