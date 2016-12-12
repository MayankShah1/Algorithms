import QuickSort
import random

# Randomized Partition function
def random_partition(array, low, high):
    i = random.randrange(low,high + 1)
    QuickSort.exchange(array, i, low)
    return QuickSort.partition(array, low, high)

# Randomized Quicksort function
def random_quicksort(array, low, high):
    ''' (list of int, int, int) -> NoneType

    Sorts the array from low to high.

    Precondtion : initial call should be
    >>> random_quicksort(array, 0, len(array) - 1)
    '''
    if low >= high:
        return
    q = random_partition(array, low, high)
    random_quicksort(array, low, q - 1)
    random_quicksort(array, q + 1, high)
