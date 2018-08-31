import numbers
from array import array


class Vector:
    typecode = 'd'

    def __init__(self, components):
        self._components = array(self.typecode, components)

    def __mul__(self, scalar):
        if isinstance(scalar, numbers.Real):
            return Vector(n * scalar for n in self)
        else:
            return NotImplemented

    def __iter__(self):
        return iter(self._components)

    def __rmul__(self, scalar):
        return self * scalar

    def __repr__(self):
        return 'Vector {}'.format(', '.join(map(str, self._components)))


if __name__ == '__main__':
    print(Vector([1.0, 2.0, 3.0]) * 12)
    print(10 * Vector([1, 2, 3, 4, 5]))
