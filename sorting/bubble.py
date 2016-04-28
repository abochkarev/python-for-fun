def bubble(l):
    while True:
        sorted = True
        for i in range(len(l) - 1):
            if l[i] > l[i + 1]:
                l[i], l[i + 1] = l[i + 1], l[i]
                sorted = False
        if sorted:
            break
    return l


print bubble([3, 1, 4, 6, 7, 2, 5, 7, 2, 5, 7, 89, 0, 2, 4])
