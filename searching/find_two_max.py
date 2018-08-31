# find two max elements in a single pass
def find_two_max(l):
    max_1, max_2 = l[0], l[1]
    if max_2 < max_1:
        max_1, max_2 = max_2, max_1
    for i in range(2, len(l)):
        if max_2 < l[i]:
            max_1, max_2 = max_2, l[i]
        if max_1 < l[i] and max_2 != l[i]:
            max_1 = l[i]
    return max_1, max_2


print
find_two_max([61, 99, 2, 33, 122, 11])
