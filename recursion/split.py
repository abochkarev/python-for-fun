# split a list of lists on small lists
def split(lst):
    def collect(l, tmp=[], res=[]):
        for i in l:
            if isinstance(i, list):
                collect(i, [], res)
            else:
                tmp.append(i)
        res.append(tmp)

    result = []
    collect(lst, [], result)
    return result


print split([1, [2], 3, [2, 3, 4, [4], 5], [6, 7, 8, 9, 0, [1, 2, 3, [4, 5, 6, 7, [6]]]]])
