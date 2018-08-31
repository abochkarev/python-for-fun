import itertools


class Vector:
    def __init__(self, elems):
        if elems is None:
            self._elems = []
        else:
            self._elems = list(elems)

    def __iter__(self):
        return iter(self._elems)

    def __add__(self, other):
        el = itertools.zip_longest(self, other, fillvalue=0)
        return Vector((a + b for a, b in el))

    def __repr__(self):
        return ", ".join(map(str, self._elems))


if __name__ == "__main__":
    v1 = Vector((1, 2, 3, 4, 5))
    v2 = Vector((1, 2, 3))
    print(v1 + v2)
