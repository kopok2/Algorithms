import unittest
import random
import time
from LinearSearch import linear_search
from BinarySearch import binary_search
from JumpSearch import jump_search
from InterpolationSearch import interpolation_search
from ExponentialSearch import exponential_search
from TernarySearch import ternary_search


def timing(f):
    def wrap(*args):
        time1 = time.time()
        ret = f(*args)
        time2 = time.time()
        print('{:s} function took {:.3f} ms'.format(f.__name__, (time2-time1)*1000.0))

        return ret
    return wrap


TEST_ARRAYS_COUNT = random.randrange(20, 1000)


class SearchingTest(unittest.TestCase):
    @timing
    def test_linear_search(self):
        for x in range(TEST_ARRAYS_COUNT):
            array = [random.randrange(0, 1000) for y in range(x * 10 + 1)]
            array.sort()
            searched_index = random.randrange(0, len(array))
            searched_value = array[searched_index]
            self.assertEqual(array[searched_index], array[linear_search(array, searched_value)])

    @timing
    def test_binary_search(self):
        for x in range(TEST_ARRAYS_COUNT):
            array = [random.randrange(0, 1000) for y in range(x * 10 + 1)]
            array.sort()
            searched_index = random.randrange(0, len(array))
            searched_value = array[searched_index]
            self.assertEqual(array[searched_index], array[binary_search(array, searched_value)])

    @timing
    def test_jump_search(self):
        for x in range(TEST_ARRAYS_COUNT):
            array = [random.randrange(0, 1000) for y in range(x * 10 + 1)]
            array.sort()
            searched_index = random.randrange(0, len(array))
            searched_value = array[searched_index]
            self.assertEqual(array[searched_index], array[jump_search(array, searched_value)])

    @timing
    def test_interpolation_search(self):
        for x in range(TEST_ARRAYS_COUNT):
            array = [random.randrange(0, 1000) for y in range(x * 10 + 1)]
            array.sort()
            searched_index = random.randrange(0, len(array))
            searched_value = array[searched_index]
            self.assertEqual(array[searched_index], array[interpolation_search(array, searched_value)])

    @timing
    def test_exponential_search(self):
        for x in range(TEST_ARRAYS_COUNT):
            array = [random.randrange(0, 1000) for y in range(x * 10 + 1)]
            array.sort()
            searched_index = random.randrange(0, len(array))
            searched_value = array[searched_index]
            self.assertEqual(array[searched_index], array[exponential_search(array, searched_value)])

    @timing
    def test_ternary_search(self):
        for x in range(TEST_ARRAYS_COUNT):
            array = [random.randrange(0, 1000) for y in range(x * 10 + 1)]
            array.sort()
            searched_index = random.randrange(0, len(array))
            searched_value = array[searched_index]
            self.assertEqual(array[searched_index], array[ternary_search(array, searched_value)])


if __name__ == "__main__":
    print("Testing algorithms on {0} random test arrays.".format(TEST_ARRAYS_COUNT))
    unittest.main()
