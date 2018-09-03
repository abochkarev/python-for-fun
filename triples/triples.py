import collections
import sys


def triples(n):
    l = range(1, n)
    res = collections.OrderedDict()
    for i in l:
        for j in l:
            s = i + j
            if s < n:
                res[tuple(sorted((i, j, s)))] = None
    print(res.keys())


if __name__ == '__main__':
    triples(int(sys.argv[1]))

