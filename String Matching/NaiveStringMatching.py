def naive_string_match(text, pattern):
    ''' (str, str) -> list of int

    Returns a list of shifts in text to find occurence of
    pattern in text.

    >>> naive_string_match('ATGCTGCUATGC','TGC')
    [1, 4, 9]

    '''
    shifts = []

    for i in range(len(text) - len(pattern) + 1):
        matched_characters = 0
        for j in range(len(pattern)):
            if text[i + j] == pattern[j]:
                matched_characters = matched_characters + 1
        if matched_characters == len(pattern):
            shifts.append(i)

    return shifts

