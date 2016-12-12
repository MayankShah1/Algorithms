# Naive string matching algorithm using find function
def naive_string_matching_find(text, pattern):
    ''' (str, str) -> list of int

    Returns a list of shifts in text to find occurence of
    pattern in text.

    >>> naive_string_matching_find('ATGCTGCUATGC','TGC')
    [1, 4, 9]

    '''
    shifts = []

    shift = text.find(pattern)
    while shift != -1:
        shifts.append(shift)
        shift = text.find(pattern, shift + 1)

    return shifts

print(naive_string_matching_find('ATGCTGCUATGC','TGC'))
