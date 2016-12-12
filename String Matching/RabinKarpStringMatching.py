def rabin_karp_string_match(text, pattern):
    ''' (str, str, int, int) -> list of int

    Returns a list of shifts in text to find occurence of
    pattern in text.

    >>> rabin_karp_string_match('ATGCTGCUATGC','TGC')
    [1, 4, 9]

    '''
    shifts = []
    n = len(text)
    m = len(pattern)

    # Preprocessing
    p = hash(pattern)
    t = hash(text[:m])

    # Checking for string match
    for shift in range(n - m + 1):
        #print('P : ' , p , ' T : ', t)
        if p ==  t :
            matched_characters = 0
            for i in range(m):
                if text[shift + i] == pattern[i]:
                    matched_characters = matched_characters + 1
            if matched_characters == m:
                shifts.append(shift)
        if shift < n - m:
            t = hash(text[shift + 1 : shift + m + 1])

    return shifts

print(rabin_karp_string_match('ATGCTGCUATGC','TGC'))

