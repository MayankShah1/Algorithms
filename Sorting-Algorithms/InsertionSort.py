def insertion_sort(array):
    '''(list of int) -> NoneType

    Sorts the elements of array in non-decreasing order.

    >>> insertion_sort([4, 2, 1, 3, 5])
    Sorts the list as [1, 2, 3, 4, 5]

    '''
    for j in range(1,len(array)):
        key_element = array[j]

        # Insert array[j] to the sorted part
        i = j - 1
        while i >= 0 and array[i] > key_element:
            array[i + 1] = array[i]
            i = i - 1
            
        array[i + 1] = key_element
