import unittest
from array_list import ArrayList

class TestArrayList(unittest.TestCase):
    def setUp(self):
        self.lst = ArrayList()

    def test_length(self):
        self.assertEqual(self.lst.length(), 0)
        self.lst.append('a')
        self.assertEqual(self.lst.length(), 1)

    def test_append(self):
        self.lst.append('a')
        self.assertEqual(self.lst.get(0), 'a')
        with self.assertRaises(ValueError):
            self.lst.append('ab')
        with self.assertRaises(ValueError):
            self.lst.append(1)

    def test_insert(self):
        self.lst.append('a')
        self.lst.insert('b', 1)
        self.assertEqual(self.lst.get(1), 'b')
        self.lst.insert('c', 0)
        self.assertEqual(self.lst.get(0), 'c')
        with self.assertRaises(IndexError):
            self.lst.insert('d', 10)
        with self.assertRaises(IndexError):
            self.lst.insert('d', -1)
        with self.assertRaises(ValueError):
            self.lst.insert('ab', 0)

    def test_delete(self):
        self.lst.append('a')
        self.lst.append('b')
        self.assertEqual(self.lst.delete(0), 'a')
        self.assertEqual(self.lst.length(), 1)
        with self.assertRaises(IndexError):
            self.lst.delete(10)
        with self.assertRaises(IndexError):
            self.lst.delete(-1)

    def test_deleteAll(self):
        for ch in 'aabbcc':
            self.lst.append(ch)
        self.lst.deleteAll('b')
        self.assertEqual(self.lst.length(), 4)
        self.assertEqual(self.lst.get(0), 'a')
        self.assertEqual(self.lst.get(2), 'c')
        self.lst.deleteAll('x')  # no effect
        self.assertEqual(self.lst.length(), 4)
        with self.assertRaises(ValueError):
            self.lst.deleteAll('ab')

    def test_get(self):
        self.lst.append('a')
        self.assertEqual(self.lst.get(0), 'a')
        with self.assertRaises(IndexError):
            self.lst.get(1)
        with self.assertRaises(IndexError):
            self.lst.get(-1)

    def test_clone(self):
        for ch in 'abc':
            self.lst.append(ch)
        clone = self.lst.clone()
        self.assertEqual(clone.length(), 3)
        self.assertEqual(clone.get(1), 'b')
        clone.append('d')
        self.assertEqual(self.lst.length(), 3)
        self.assertEqual(clone.length(), 4)

    def test_reverse(self):
        for ch in 'abc':
            self.lst.append(ch)
        self.lst.reverse()
        self.assertEqual(self.lst.get(0), 'c')
        self.assertEqual(self.lst.get(2), 'a')

    def test_findFirst(self):
        for ch in 'abac':
            self.lst.append(ch)
        self.assertEqual(self.lst.findFirst('a'), 0)
        self.assertEqual(self.lst.findFirst('c'), 3)
        self.assertEqual(self.lst.findFirst('x'), -1)
        with self.assertRaises(ValueError):
            self.lst.findFirst('ab')

    def test_findLast(self):
        for ch in 'abac':
            self.lst.append(ch)
        self.assertEqual(self.lst.findLast('a'), 2)
        self.assertEqual(self.lst.findLast('c'), 3)
        self.assertEqual(self.lst.findLast('x'), -1)
        with self.assertRaises(ValueError):
            self.lst.findLast('ab')

    def test_clear(self):
        for ch in 'abc':
            self.lst.append(ch)
        self.lst.clear()
        self.assertEqual(self.lst.length(), 0)

    def test_extend(self):
        for ch in 'abc':
            self.lst.append(ch)
        other = ArrayList()
        for ch in 'de':
            other.append(ch)
        self.lst.extend(other)
        self.assertEqual(self.lst.length(), 5)
        self.assertEqual(self.lst.get(3), 'd')
        self.assertEqual(self.lst.get(4), 'e')
        other.append('f')
        self.assertEqual(self.lst.length(), 5)  # не змінюється
        with self.assertRaises(ValueError):
            self.lst.extend([1,2,3])

if __name__ == '__main__':
    unittest.main() 