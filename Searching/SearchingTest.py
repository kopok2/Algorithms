import unittest
import random
from LinearSearch import linear_search
from BinarySearch import binary_search


class SearchingTest(unittest.TestCase):
    def test_linear_search(self):
        array = [1, 2, 3, 4, 5]
        result = linear_search(array, 3)
        self.assertEqual(2, result)

    def test_binary_search(self):
        for x in range(random.randrange(20, 100)):
            array = [random.randrange(0, 1000) for y in range(x + 10)]
            array.sort()
            searched_index = random.randrange(0, len(array))
            searched_value = array[searched_index]
            self.assertEqual(array[searched_index], array[binary_search(array, searched_value)])


if __name__ == "__main__":
    unittest.main()
