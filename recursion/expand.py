# expand a list of lists
def expand(l):
    if isinstance(l, list):
        return expand(l[0]) + expand(l[1:]) if len(l) > 0 else []
    else:
        return [l]


print
expand([1, 2, 3, 4, 5, 6, 7, [1, 2, 3, 4, [], 6, 7, 8, 9], 10, 11, 12, 13, 14])
