class ArythmeticProgression:
    
    def __init__(self, begin, step, end=None):
        self.begin = begin
        self.step = step
        self.end = end 

    def __iter__(self):
        result = type(self.begin + self.step)(self.begin)
        forever = self.end is None
        index = 0
        while forever or result < self.end:
            yield result
            index += self.begin + self.step * index


a = ArythmeticProgression(1, 2, 100)
for i in a:
    print(i)