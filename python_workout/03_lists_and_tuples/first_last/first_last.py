def firstlast(seq):
    first, last = seq[:1], seq[-1:]
    return first + last


assert firstlast('abc') == 'ac'
assert firstlast([1,2,3,4]) == [1, 4]
