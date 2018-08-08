class Averager:
    def __init__(self):
        self.series = []

    def __call__(self, new_value):
        self.series.append(new_value)
        total = sum(self.series)
        return total/len(self.series)



def make_averager():
    series = []

    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total/len(series)

    return averager

avg1 = Averager()
avg2 = make_averager()

print (avg1(1))
print (avg1(2))
print (avg1(3))

print (avg2(1))
print (avg2(2))
print (avg2(3))


