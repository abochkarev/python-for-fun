# change negative elements to 0
def change(l):
    if isinstance(l, list):
        return [change(l[0])] + change(l[1:]) if len(l) > 0 else []
    else:
        return max(l, 0)


print change([-1, -2, -3, -3, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, [1, 2, 3, 4, [1, 2, 3, 4]]])
