import abc
import random

class Tombola(abc.ABC):

    @abc.abstractmethod
    def load(self, iterable):
        """Load"""

    @abc.abstractmethod
    def pick(self):
        """Load"""

    def loaded(self):
        return bool(self.inspect())

    def inspect(self):
        items = []
        while True:
            try:
                items.append(self.pick())
            except LookupError:
                break
        
        self.load(items)
        return tuple(sorted(items))




class BingoCage(Tombola):
    def __init__(self, items):
        self._randomizer = random.SystemRandom()
        self._items = []
        self.load(items)

    def load(self, items):
        self._items.extend(items)
        self._randomizer.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')
    def __call__(self):
        self.pick()
    
    def __repr__(self):
        return "%s" % self._items
if __name__ == "__main__":
    b = BingoCage([1, 2, 3, 4, 5, 6, 7])
    b.pick()
    print (b)
