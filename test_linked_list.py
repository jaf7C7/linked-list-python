from unittest import TestCase
from linked_list import LinkedList


class TestInsert(TestCase):

    def test_insert_adds_a_node_with_the_given_value(self):
        ll = LinkedList()
        ll.insert(1)
        self.assertEqual(1, ll.head.value)

    def test_insert_preserves_ascending_order_of_node_values(self):
        ll = LinkedList()
        ll.insert(3)
        ll.insert(1)
        self.assertEqual(1, ll.head.value)


class TestIter(TestCase):

    def test_is_implemented(self):
        ll = LinkedList()
        ll.insert(3)
        ll.insert(5)
        ll.insert(9)
        values = []
        for node in ll:
            values.append(node.value)
        self.assertEqual([3, 5, 9], values)


class TestGetItem(TestCase):

    def test_is_implemented(self):
        ll = LinkedList()
        ll.insert(3)
        self.assertEqual(3, ll[3].value)

    def test_raises_IndexError_if_index_not_found(self):
        ll = LinkedList()
        with self.assertRaises(IndexError):
            ll[3]


class TestDelItem(TestCase):

    def test_is_implemented(self):
        ll = LinkedList()
        ll.insert(3)
        del ll[3]
        self.assertIs(None, ll.head)

    def test_raises_IndexError_if_index_not_found(self):
        ll = LinkedList()
        with self.assertRaises(IndexError):
            del ll[3]
