# Recursive Merge-Sort function
def merge_sort(array, low, high):

    if low >= high:
        return
    
    mid = low + (high - low) // 2
    merge_sort(array, low, mid)
    merge_sort(array, mid+1, high)
    # Call merge procedure
    merge(array, low, mid, high)

# Merge procedure
def merge(array, low, mid, high):
    
    # left array
    left_array = []
    for i in range(low, mid + 1):
        left_array.append(array[i])

    # right array
    right_array = []
    for i in range(mid + 1, high + 1):
        right_array.append(array[i])
        
    i = 0
    j = 0

    for k in range(low, high + 1):
        if i >= len(left_array) and  j < len(right_array):
            array[k] = right_array[j]
            j = j + 1
        elif j >= len(right_array) and i < len(left_array):
            array[k] = left_array[i]
            i = i + 1
        elif left_array[i] <= right_array[j]:
            array[k] = left_array[i]
            i = i + 1
        else :
            array[k] = right_array[j]
            j = j + 1
