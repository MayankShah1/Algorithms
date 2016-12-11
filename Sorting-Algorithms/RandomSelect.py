# import QuickSort to use partition function
import QuickSort

# Quick Select function
def quickselect(array, low, high, i):
    ''' (list of int, int, int, int) -> int

    Returns the i_th smallest element in array.
    
    >>> quickselect([4, 1, 3, 2, 5], 0, 4, 2)
    2
    '''
    if low >= high:
        return array[low]

    q = QuickSort.partition(array, low, high)
    # k = rank(array[q])
    k = q - low + 1

    if i == k:
        return array[q]
    elif i < k:
        return quickselect(array, low, q - 1, i)
    else:
        return quickselect(array, q + 1, high, i - k)


    
