# Compute the prefix function for the pattern
def compute_transition_function(pattern):
    ''' (str) -> list of int

    Return the prefix function of the pattern.

    >>> compute_transition_function('ababaca')
    [0, 0, 1, 2, 3, 0, 1]
    '''
    m = len(pattern)
    prefix_function = [0] * m
    k = 0
    for i in range(1,m):
        while k > 0 and pattern[k] != pattern[i]:
            k = prefix_function[k]
            
        if pattern[k] == pattern[i]:
            k = k + 1

        prefix_function[i] = k

    return prefix_function


# Match the string
def KMP_matcher(text, pattern):
    ''' (str, str, int, int) -> list of int

    Returns a list of shifts in text to find occurence of
    pattern in text.

    >>> KMP_matcher('ATGCTGCUATGC','TGC')
    [1, 4, 9]

    '''
    n = len(text)
    m = len(pattern)
    shifts = []
    
    prefix_list = compute_transition_function(pattern)
    k = 0
    
    for i in range(n):
        while k > 0 and pattern[k] != text[i]:
            k = prefix_list[k - 1]

        if pattern[k] == text[i]:
            k = k + 1

        if k == m:
            shifts.append(i - m + 1)
            k = prefix_list[k - 1]

    return shifts
