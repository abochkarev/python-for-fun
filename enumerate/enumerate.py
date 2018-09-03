def enumerat(lst):
    print([(i, lst[i]) for i in range(len(lst))])


if __name__ == '__main__':
    enumerat(["a", "b", "c"])
