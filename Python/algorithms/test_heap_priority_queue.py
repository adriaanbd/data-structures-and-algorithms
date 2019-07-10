from unittest import TestCase, main
from heap_priority_queue import Heap
from pdb import set_trace


class TestHeap(TestCase):
    def setUp(self):
        self.heap = Heap(2)

    def test_init_heap(self):
        self.assertIsInstance(self.heap, Heap)

    def test_init_attrs(self):
        self.assertEqual(self.heap.array, [None, None])
        self.assertEqual(self.heap.next_idx, 0)

    def test_insert_one(self):
        self.heap.insert(0)
        self.assertEqual(self.heap.array, [0, None])
        self.assertEqual(self.heap.next_idx, 1)

    def test_handle_max_capacity(self):
        self.heap.insert(0)
        self.heap.insert(1)
        self.assertEqual(self.heap.next_idx, 2)
        self.assertEqual(self.heap.array, [0, 1, None, None])


if __name__ == '__main__':
    main()