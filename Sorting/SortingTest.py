import unittest
import random
import time
from SelectionSort import selection_sort
from BubbleSort import bubble_sort
from InsertionSort import insertion_sort
from MergeSort import merge_sort
from HeapSort import heap_sort
from QuickSort import quick_sort
from CountingSort import counting_sort
from RadixSort import radix_sort


def timing(f):
    def wrap(*args):
        time1 = time.time()
        ret = f(*args)
        time2 = time.time()
        print('{:s} function took {:.3f} ms'.format(f.__name__, (time2-time1)*1000.0))

        return ret
    return wrap


TEST_ARRAYS_COUNT = 20


class SortingTest(unittest.TestCase):
    @timing
    def test_selection_sort(self):
        for x in range(TEST_ARRAYS_COUNT):
            array = [random.randrange(0, 1000) for y in range(x * 100 + 1)]
            unsorted = array.copy()
            unsorted.sort()
            selection_sort(array)
            self.assertEqual(unsorted, array)

    @timing
    def test_bubble_sort(self):
        for x in range(TEST_ARRAYS_COUNT):
            array = [random.randrange(0, 1000) for y in range(x * 100 + 1)]
            unsorted = array.copy()
            unsorted.sort()
            bubble_sort(array)
            self.assertEqual(unsorted, array)

    @timing
    def test_insertion_sort(self):
        for x in range(TEST_ARRAYS_COUNT):
            array = [random.randrange(0, 1000) for y in range(x * 100 + 1)]
            unsorted = array.copy()
            unsorted.sort()
            insertion_sort(array)
            self.assertEqual(unsorted, array)

    @timing
    def test_merge_sort(self):
        for x in range(TEST_ARRAYS_COUNT):
            array = [random.randrange(0, 1000) for y in range(x * 100 + 1)]
            unsorted = array.copy()
            unsorted.sort()
            merge_sort(array)
            self.assertEqual(unsorted, array)

    @timing
    def test_heap_sort(self):
        for x in range(TEST_ARRAYS_COUNT):
            array = [random.randrange(0, 1000) for y in range(x * 100 + 1)]
            unsorted = array.copy()
            unsorted.sort()
            heap_sort(array)
            self.assertEqual(unsorted, array)

    @timing
    def test_quick_sort(self):
        for x in range(TEST_ARRAYS_COUNT):
            array = [random.randrange(0, 1000) for y in range(x * 100 + 1)]
            unsorted = array.copy()
            unsorted.sort()
            quick_sort(array)
            self.assertEqual(unsorted, array)

    @timing
    def test_counting_sort(self):
        for x in range(TEST_ARRAYS_COUNT):
            array = [random.randrange(0, 1000) for y in range(x * 100 + 1)]
            unsorted = array.copy()
            unsorted.sort()
            counting_sort(array)
            self.assertEqual(unsorted, array)

    @timing
    def test_radix_sort(self):
        for x in range(TEST_ARRAYS_COUNT):
            array = [random.randrange(0, 1000) for y in range(x * 1000 + 1)]
            unsorted = array.copy()
            unsorted.sort()
            radix_sort(array)
            self.assertEqual(unsorted, array)


if __name__ == "__main__":
    print("Testing algorithms on {0} random test arrays.".format(TEST_ARRAYS_COUNT))
    unittest.main()
