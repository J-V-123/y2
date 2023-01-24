import unittest

from linked_list import LinkedListException, LinkedList, Empty, Cell


class TestIsEmptyAndLength(unittest.TestCase):

    empty = Empty()
    cell_1 = Cell('abc', empty)

    def testEmptyOnEmpty(self):
        self.assertEqual(TestIsEmptyAndLength.empty.is_empty(), True)

    def testEmptyOnCell(self):
        self.assertEqual(TestIsEmptyAndLength.cell_1.is_empty(), False)

    def testLengthOnEmpty(self):
        self.assertEqual(TestIsEmptyAndLength.empty.length(), 0)

    def testLengthOnCell(self):
        self.assertEqual(TestIsEmptyAndLength.cell_1.length(), 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
