# Partition function
def partition(array, low, high):
    ''' (list of int, int , int) -> int

    Returns a pivot element(x) such that array[low..x - 1] <= array[x]
    and array[x + 1, high] >= array[x]
    
    '''
    pivot = array[low]
    i = low

    for j in range(low + 1, high + 1):
        if array[j] <= pivot:
            i = i + 1
            exchange(array, i , j)

    exchange(array, low, i)
    return i

# Quicksort function
def quicksort(array, low, high):
    ''' (list of int, int, int) -> NoneType

    Sorts the array from low to high.

    Precondtion : initial call should be
    >>> quicksort(array, 0, len(array) - 1)
    '''
    if low >= high:
        return
    q = partition(array, low, high)
    quicksort(array, low, q - 1)
    quicksort(array, q + 1, high)

# Exchange
def exchange(array, i , j):
    '''(list of int, int, int) -> NoneType

    >>> exchange([1, 2, 3, 4], 1, 3)
    Makes the list [1, 4, 3, 2]

    '''
    temp = array[i]
    array[i] = array[j]
    array[j] = temp
