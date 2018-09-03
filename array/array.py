import sys


def array(n, m):
    return [[None] * n for i in range(m)]


if __name__ == '__main__':
    print(array(int(sys.argv[1]), int(sys.argv[2])))
