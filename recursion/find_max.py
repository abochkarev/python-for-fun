# find max value in a list of lists
def find_max(l, result=[]):
    for i in l:
        if isinstance(i, list):
            find_max(i, result)
        else:
            result.append(i)
    return max(result)


print find_max(
    [1, 2, 3, [[234], [1, 24, 4, 5], [12, 3, 4, 5]], 4, 5, 6, 7, [88, 2, 3, 4, [89], 6, 7, 8, 9], 10, 11, 12, 13, 14])
