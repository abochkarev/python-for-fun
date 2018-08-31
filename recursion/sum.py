# calculate sum of elements in a list of lists
def calculate_sum(l):
    if isinstance(l, list):
        return calculate_sum(l[0]) + calculate_sum(l[1:]) if len(l) > 0 else 0
    else:
        return l


print
calculate_sum([1, 2, 3, [4, 5, 6]])
