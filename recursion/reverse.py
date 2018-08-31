# reverse a list of lists
def reverse(l):
    if isinstance(l, list):
        return reverse(l[1:]) + [reverse(l[0])] if len(l) > 0 else []
    else:
        return l


print
reverse([1, 2, 3, 4, 5, 6, 7, [1, 2, 3, 4, [], 6, 7, 8, 9], 10, 11, 12, 13, 14])
